# coding: utf-8
import fnmatch
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import glob



#house keeping, delete old files that are no longer needed
for png in glob.glob('/home/coaxlab/Dropbox/r2d4/behavior/*Days1-*.png'):
    os.remove(png)

summary_files = []
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*summary*.csv'):
        summary_files.append(file)
#get unique subjects
subs = []
for i in range(0, len(summary_files)):
    subs.append(summary_files[i][:4])
uniqueSubs = list(set(subs))

# Now find summary files relating to that subject only
# Get the data for the RT, accuracy, and autocorrelation results
for sub in uniqueSubs:
    Acc = pd.DataFrame(columns=('Day', 'randAcc', 'seqAcc'))
    RT = pd.DataFrame(columns = ('Day', 'zscoredRT'))
    lag_names = ['lag' + str(i) for i in  range(1,32)]
    randLags = pd.DataFrame(columns = lag_names)
    seqLags = pd.DataFrame(columns = lag_names)
    df = pd.DataFrame()
    sub_files = []

    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*'+sub+'*summary*.csv'):
            sub_files.append(file)
    for day in sub_files:
        df = pd.read_csv(day)
        Acc.loc[int(day[day.find('Day')+4:-4])] = [int(day[day.find('Day')+4:-4]),df['accuracy'][5], df['accuracy'][6]]
        zscoreRT = (df['rt_all'][5] - df['rt_all'][6])/df['sdRT'][5]
        RT.loc[int(day[day.find('Day')+4:-4])] = [int(day[day.find('Day')+4:-4]), zscoreRT]
        randLags.loc[int(day[day.find('Day')+4:-4])] = df[lag_names].loc[5]
        seqLags.loc[int(day[day.find('Day')+4:-4])] = df[lag_names].loc[6]
    randLags = randLags.sort(axis=0)
    seqLags = seqLags.sort(axis=0)

    # Generate autocorrelation plots
    fig = plt.figure()
    blues = plt.get_cmap('Blues')
    # Random
    for i in range(1,len(randLags)+1):
        colorBlue = blues(.15 + float(i)/(len(randLags)+1))
        plt.plot(range(1,32),randLags.loc[i], color = colorBlue, label = 'Day ' + str(i))

    sns.set_style("darkgrid")

    randPlotFN = day[:4] + '_randCorr_Days1-' + str(len(Acc))
    plt.xlabel('Lag (Trials)', fontsize=18)
    plt.ylabel('Correlation', fontsize=16)
    plt.legend()
    plt.axis([0,32, -0.5,1])
    plt.savefig(randPlotFN)
    plt.close("all")
    # Sequence
    greens = plt.get_cmap('Greens')
    for i in range(1,len(randLags)+1):
        colorGreen = greens(.15 + float(i)/(len(randLags)+1))
        plt.plot(range(1,32),seqLags.loc[i], color = colorGreen, label = 'Day ' + str(i))

    seqPlotFN = day[:4] + '_seqCorr_Days1-' + str(len(Acc))
    plt.xlabel('Lag (Trials)', fontsize=18)
    plt.ylabel('Correlation', fontsize=16)
    plt.legend()
    plt.axis([0,32, -0.5,1])
    plt.savefig(seqPlotFN)
    plt.close("all")

    #Generate Accuracy Plots for the Sequence
    Acc.sort(['Day'], ascending =[True], inplace=True)
    accPlot_fn =  day[:4] + '_Acc_Days1-' + str(len(Acc))
    plt.figure(figsize=(8, 6))
    sns.lmplot('Day', 'seqAcc',data=Acc, fit_reg=False)
    plt.axis([0,len(Acc)+1,.5,1])
    plt.ylabel('% Correct', fontsize=16)
    plt.xlabel('Day', fontsize = 18)
    plt.savefig(accPlot_fn)
    plt.close("all")

    #Generate RT plots
    RT.sort(['Day'], ascending =[True], inplace=True)
    RTPlot_fn =  day[:4] + '_RT_Days1-' + str(len(Acc))
    plt.figure(figsize=(8, 6))
    sns.lmplot('Day', 'zscoredRT',data=RT, fit_reg=False)
    plt.axis([0,len(RT)+1,-1,10])
    plt.ylabel('Reaction Times (z-scores)', fontsize=16)
    plt.xlabel('Day', fontsize = 18)
    plt.savefig(RTPlot_fn)
    plt.close("all")

#Send the updated results to email
fromaddr = 'beuk.pat@gmail.com'
toaddrs  = 'beuk.pat@gmail.com'
msg = 'r2d4 updated summary'

msg = MIMEMultipart()
msg['Subject'] = 'R2D4 Updated Summary'
msg['From'] = 'beuk.pat@gmail.com'
msg['To'] = 'beuk.pat@gmail.com'
msg.preamble = ''

# Credentials (if needed)
username = 'beuk.pat'
password = ''
for file in glob.glob('*.png'):
    fp = open(file, 'rb')
    img = MIMEImage(fp.read(), name=os.path.basename(file))
    fp.close()
    msg.attach(img)

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg.as_string())
server.quit()
