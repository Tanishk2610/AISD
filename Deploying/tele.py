import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from datetime import datetime
import cnn_modelarr as cnn

# AISD
bot = telebot.TeleBot("SECRET_API_KEY")
dis_type = "Model Identifies\n◉ Kidney\n    ➢ Cyst\n    ➢ Stone\n    ➢ Tumor\n    ➢ Normal\n◉ BrainTumor\n    ➢ Glioma\n    ➢ Meningioma\n    ➢ Pituitary\n    ➢ Normal\n◉ Lungs\n    ➢ Covid\n    ➢ Lung_Opacity\n    ➢ Viral_Pneumonia\n    ➢ Normal\n◉ Tuberculosis\n    ➢ Positive\n    ➢ Negative"
com_list = "Use the following Commands \n/types ➢ It shows all the diseases available for detection \n/help ➢ It helps you to solve a problem \n/moreinfo ➢ Gives the detail description of the Model"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_name = message.from_user.first_name
    bot.send_message(message.chat.id, "Hello " + chat_name + ", Welcome to AI-Smart Diagnosis\n\nJust click a picture and send it. I can identify the disease based on my knowledge.")
    bot.send_message(message.chat.id, com_list)

@bot.message_handler(commands=['types'])
def disease_types(message):
    bot.send_message(message.chat.id, dis_type)

@bot.message_handler(commands=['test'])
def send_test(message):
    bot.send_message(message.chat.id, message.chat.id)

@bot.message_handler(commands=['report'])
def send_report(message):
    bot.send_message(message.from_user.id, "Report requested by " + str(message.from_user.first_name))

@bot.message_handler(content_types=['document'])
def upload_photo(message):
    date = datetime.utcfromtimestamp(message.date + 19800).strftime('%Y%m%d_%H%M%S')
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    btn1 = KeyboardButton("Kidney")
    btn2 = KeyboardButton("Lungs")
    btn3 = KeyboardButton("Brain")
    btn4 = KeyboardButton("Tuberculosis")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    sent = bot.send_message(message.chat.id, "Choose your Disease type", reply_markup = markup)
    raw = message.document.file_id
    file_info = bot.get_file(raw)
    file = bot.download_file(file_info.file_path)
    fl_name = "Img-" + date + "_" + str(message.from_user.id) + ".jpg"
    with open(fl_name,'wb') as new_file:
        new_file.write(file)
    bot.register_next_step_handler(sent, which_model1, fl_name)

def which_model1(message, fl_name):
    bot.send_message(message.chat.id, "Plz wait your result is generating")
    if message.text == "Kidney":
        pred = cnn.Model_Kidney(fl_name)
    elif message.text == "Brain":
        pred = cnn.Model_Brain(fl_name)
    elif message.text == "Lungs":
        pred = cnn.Model_Lungs(fl_name)
    elif message.text == "Tuberculosis":
        pred = cnn.Model_Tuber(fl_name)
    rmmark = ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "<strong>Result</strong>: " + pred[0], parse_mode="HTML", reply_markup=rmmark)
    os.remove(fl_name)
    rchatid = str(message.from_user.id)
    rfname = str(message.from_user.first_name)
    rlname = str(message.from_user.last_name or "")
    runame = str(message.from_user.username)
    rdate = datetime.utcfromtimestamp(message.date + 19800).strftime('%Y-%m-%d %I:%M:%S %p')
    rmodel = str(message.text)
    rdis = str(pred[1])
    rfl = open("datarecord.csv","a")
    rfl.write(rchatid + "," + rfname + "," + rlname + "," + runame + "," + rdate + "," + rmodel + "," + rdis + "\n")
    rfl.close()

@bot.message_handler(content_types=['photo'])
def upload_photo(message):
    date = datetime.utcfromtimestamp(message.date + 19800).strftime('%Y%m%d_%H%M%S')
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    btn1 = KeyboardButton("Kidney")
    btn2 = KeyboardButton("Lungs")
    btn3 = KeyboardButton("Brain")
    btn4 = KeyboardButton("Tuberculosis")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    sent = bot.send_message(message.chat.id, "Choose your Disease type", reply_markup = markup)
    raw = message.photo[2].file_id
    file_info = bot.get_file(raw)
    file = bot.download_file(file_info.file_path)
    fl_name = "Img-" + date + "_" + str(message.from_user.id) + ".jpg"
    with open(fl_name,'wb') as new_file:
        new_file.write(file)
    bot.register_next_step_handler(sent, which_model2, fl_name)

def which_model2(message, fl_name):
    bot.send_message(message.chat.id, "Plz wait your result is generating")
    if message.text == "Kidney":
        pred = cnn.Model_Kidney(fl_name)
    elif message.text == "Brain":
        pred = cnn.Model_Brain(fl_name)
    elif message.text == "Lungs":
        pred = cnn.Model_Lungs(fl_name)
    elif message.text == "Tuberculosis":
        pred = cnn.Model_Tuber(fl_name)
    rmmark = ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "<strong>Result</strong>: " + pred[0], parse_mode="HTML", reply_markup=rmmark)
    os.remove(fl_name)
    rchatid = str(message.from_user.id)
    rfname = str(message.from_user.first_name)
    rlname = str(message.from_user.last_name or "")
    runame = str(message.from_user.username)
    rdate = datetime.utcfromtimestamp(message.date + 19800).strftime('%Y-%m-%d %I:%M:%S %p')
    rmodel = str(message.text)
    rdis = str(pred[1])
    rfl = open("datarecord.csv","a")
    rfl.write(rchatid + "," + rfname + "," + rlname + "," + runame + "," + rdate + "," + rmodel + "," + rdis + "\n")
    rfl.close()

print("Running")
bot.infinity_polling()
