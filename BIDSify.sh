#! /bin/bash

# We are aiming for this file structure (see the docs for details) http://bids.neuroimaging.io/bids_spec1.0.2.pdf
#  /source_data
#   README
#   participants.tsv
#   /scanner_protocol
#   /sub-01
#     /ses-pre/post
#       /anat
#         T1w
#         T2w
#         T1w.json
#         T2w.json
#       /func
#         bold
#         bold.json
#         events.tsv
#       /fmap
#         phase
#         magnitude
#         phase.json

# Requirements for openfMRI:
# 1. Deface your high res T1/T2 - this python script https://github.com/poldracklab/pydeface will do that nicely
# 2. You must follow a very precise naming convention. I wish that they hadn't used '-' in the name. I don't follow that logic.
# 3. You must have very specific hdr info if you include fieldmaps. That header info can be easily generated with Chris Rordens 
#    https://github.com/rordenlab/dcm2niix That software is included in mricrogl. So you can do command line: dcm2niix
#    /path/to/dcm/data/ that will output json files which you can either copy directly into your BIDS files or you can copy specific
#    lines. Note that one outstanding issue is the calculation of TotalReadoutTime.
# 4. Your onset files must be tsv with at minimum columns for onset time and onset duration
# 5. gzip the niis to save space.
# 6. Dirs at a lower level inherit json properties from above, such as for longitudional scans.


fmap_name=fieldmap_96_AP_2mmIsoVoxel_192FOV_66Slices
t1_name=t1_mpr_sag_iso_2pat_9degflip_TI900
t2_name=t2_spc_sag_p2_iso
id_count=1
n_subs=18 #change to your n_subs
for subject in $(seq 1 $n_subs)

do
  printf -v bids_id "%02d" ${id_count} #left padding with zeros for BIDS compliancy
  # Change this dir structure to your preference e.g. bids_${study_name} o/w you want the exact same naming conventions
  mkdir /data/bids_r2d4/sub-${bids_id}
  mkdir /data/bids_r2d4/sub-${bids_id}/ses-pre
  mkdir /data/bids_r2d4/sub-${bids_id}/ses-post
  mkdir /data/bids_r2d4/sub-${bids_id}/ses-pre/anat/
  mkdir /data/bids_r2d4/sub-${bids_id}/ses-pre/func/
  mkdir /data/bids_r2d4/sub-${bids_id}/ses-post/func/
  mkdir /data/bids_r2d4/sub-${bids_id}/ses-pre/fmap/
  mkdir /data/bids_r2d4/sub-${bids_id}/ses-post/fmap/

  for session in pre post
  do
    #case esac wtf bash.
    case $session in
    'pre')
      count=1
      ;;
    'post')
      count=2
      ;;
    esac

    nruns=6 #how many individual runs per session
    for run in $(seq 1 $nruns)
    do
      cp /data/r2d4/subjects/${subject}_${count}/RER_Run${run}_01/RER_Run${run}_01.nii \
      /data/bids_r2d4/sub-${bids_id}/ses-${session}/func/sub-${bids_id}_ses-${session}_task-cuedSFM_run-0${run}_bold.nii
      gzip /data/bids_r2d4/sub-${bids_id}/ses-${session}/func/sub-${bids_id}_ses-${session}_task-cuedSFM_run-0${run}_bold.nii
    done
    # Grabs the onsets for this subject and session and remakes them according to BIDS format
    # At minimum your onsets must contain columns for ['onset', 'duration'] with those precise names, other columns are optional
    python /data/bids_r2d4/code/bids_r2d4_onsets.py ${subject} ${session} ${bids_id}

    # Copy the phase and magnitude fieldmaps if you have them. 
    cp /data/r2d4/subjects/${subject}_${count}/${fmap_name}_01/${fmap_name}_01.nii \
    /data/bids_r2d4/sub-${bids_id}/ses-${session}/fmap/sub-${bids_id}_ses-${session}_phasediff.nii
    cp /data/r2d4/subjects/${subject}_${count}/${fmap_name}/${fmap_name}.nii \
    /data/bids_r2d4/sub-${bids_id}/ses-${session}/fmap/sub-${bids_id}_ses-${session}_magnitude.nii

    #BIDS format prefers compression for all nii
    gzip /data/bids_r2d4/sub-${bids_id}/ses-${session}/fmap/sub-${bids_id}_ses-${session}_phasediff.nii
    gzip /data/bids_r2d4/sub-${bids_id}/ses-${session}/fmap/sub-${bids_id}_ses-${session}_magnitude.nii

    # cp the json file into this directory o/w BIDS validation fails
    cp /data/bids_r2d4/fmap.json /data/bids_r2d4/sub-${bids_id}/ses-${session}/fmap/sub-${bids_id}_ses-${session}_phasediff.json
  done

  # copy highres t1/t2
  cp /data/r2d4/subjects/${subject}_1/${t1_name}/${t1_name}.nii \
  /data/bids_r2d4/sub-${bids_id}/ses-pre/anat/sub-${bids_id}_ses-pre_T1w.nii
  cp /data/r2d4/subjects/${subject}_1/${t2_name}/${t2_name}.nii \
  /data/bids_r2d4/sub-${bids_id}/ses-pre/anat/sub-${bids_id}_ses-pre_T2w.nii

  # copy json files to avoid confusion with hierarchical inheritance
  cp /data/bids_r2d4/T1w.json /data/bids_r2d4/sub-${bids_id}/ses-pre/anat/sub-${bids_id}_ses-pre_T1w.json
  cp /data/bids_r2d4/T2w.json /data/bids_r2d4/sub-${bids_id}/ses-pre/anat/sub-${bids_id}_ses-pre_T2w.json

  # Deface the high resolution t1 see https://github.com/poldracklab/pydeface, very fast and nice - this will overwrite original 
  pydeface /data/bids_r2d4/sub-${bids_id}/ses-pre/anat/sub-${bids_id}_ses-pre_T1w.nii \
  --outfile /data/bids_r2d4/sub-${bids_id}/ses-pre/anat/sub-${bids_id}_ses-pre_T1w.nii
  pydeface /data/bids_r2d4/sub-${bids_id}/ses-pre/anat/sub-${bids_id}_ses-pre_T2w.nii \
  --outfile /data/bids_r2d4/sub-${bids_id}/ses-pre/anat/sub-${bids_id}_ses-pre_T2w.nii


  # BIDS format prefers compression again
  gzip /data/bids_r2d4/sub-${bids_id}/ses-pre/anat/sub-${bids_id}_ses-pre_T1w.nii
  gzip /data/bids_r2d4/sub-${bids_id}/ses-pre/anat/sub-${bids_id}_ses-pre_T2w.nii

  let id_count=id_count+1 #takes about 5 minutes per subject to do all of this on my machine. Final dataset is 35 Gb. 
done
