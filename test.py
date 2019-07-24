import telebot
import os
import time
import pandas as pd
import plotly.graph_objects as go
import plotly
import numpy as np
import matplotlib.pyplot as plt
import plotly.io as pio
bot = telebot.TeleBot('662236064:AAG7ySdnPbEEGHWX-kJpwBrNtAbW5JTCMSg')

# @bot.message_handler(content_types=['text'])
# def get_text_message(message):
#     if message.text =='Привет':
#         for f in os.listdir('C:\\test'):
#             file = open('C:\\test\\' + f,'rb')
#             print(file)
#             bot.send_document(message.chat.id,file,None)
#             time.sleep(3)

@bot.message_handler(commands=['game'])
def message_report(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add('отчет1')
    markup.add('отчет2')
    bot.send_message(message.chat.id, 'Какой отчет хотите сформировать?',reply_markup=markup)
    bot.register_next_step_handler(message, get_rep_name)

@bot.message_handler(func=lambda mesage:'отчет1')
def ch_test(mesage):
    if mesage.text=='отчет1':
        pass
        # figure = get_fig().write_image("fig1.jpeg")

        # bot.register_next_step_handler(mesage,get_year)
        # plotly.offline.plot(figure, filename='file.html',show_link=False)
        # plotly.offline.plot_mpl(figure)


        # with open('fig1.jpeg','rb') as f:
        #     bot.send_photo(mesage.chat.id,f)


def get_rep_name(message):
    global rep_name
    rep_name = message.text
    if rep_name=='отчет1':
        f = pd.read_csv(
            'https://gist.githubusercontent.com/chriddyp/'
            'cb5392c35661370d95f300086accea51/raw/'
            '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/'
            'indicators.csv')
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True,)
        for i in f['Year'].unique():
            markup.add(str(i))
        bot.send_message(message.chat.id, 'За какой год формировать отчет',reply_markup=markup)
        bot.register_next_step_handler(message, report)




def report(message):
    global year
    year = message.text

    func_test(year).write_image("fig1.jpeg")
    with open('fig1.jpeg','rb') as f:
        bot.send_photo(message.chat.id,f)




def func_test(year):
    df = pd.read_csv(
        'https://gist.githubusercontent.com/chriddyp/'
        'cb5392c35661370d95f300086accea51/raw/'
        '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/'
        'indicators.csv')
    t = df[df['Year'] ==int(year)]
    t1 = t.groupby('Country Name')['Value'].mean()
    dt = pd.DataFrame(t1)
    a = dt.to_dict()
    print(a['Value'])
    # x = [{} for x in range(len(t1))]
    # print(x)

    trace = []

    for i in range(len(dt['Value'])):
        trace.append(go.Bar(

            y=[dt['Value'][i]],
            text=[dt.index[i]],
            name=dt.index[i]

        ))

    fig = go.Figure(

        data=trace

    )

    return fig


def get_fig():
    N = 100
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    sz = np.random.rand(N) * 30

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="markers",
        marker=go.scatter.Marker(
            size=sz,
            color=colors,
            opacity=0.6,
            colorscale="Viridis"
        )
    ))
    return fig

bot.polling(none_stop=True, interval=0)



