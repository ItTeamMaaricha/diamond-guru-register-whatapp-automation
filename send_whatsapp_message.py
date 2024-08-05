import pywhatkit as kit
import sys

def send_whatsapp_message(phone_number, message):
    # Send WhatsApp message
    kit.sendwhatmsg_instantly(phone_number, message, 10)  # 10 is a delay in seconds before the message is sent

if __name__ == "__main__":
    phone_number = sys.argv[1]
    message = sys.argv[2]
    send_whatsapp_message(phone_number, message)
