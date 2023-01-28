import telebot


token = "5860045535:AAGsoBhImhrWSuqYnXRmlcFvPrUdpLbqYwk"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello")


bot.infinity_polling()











# import jinja2
#
#
# html = open("pr123/templates/index.html").read()
# users = [{"name": "Andrew"}, {"name": "Victor"}]
#
# template = jinja2.Template(html)
#
# print(template.render(users=users))


# template = Template("name {{name}}")
#
# print(template.render(name="Andrew"))
#
#
# content = {"a": 5, "b": 2}
# tpl = "Сумма чисел {{a}} и {{b}} сумма {{a+b}}"
# out = Template(tpl).render(content)
# print(out)
#
# tpl = """{{title}}
#         {{'-' * title|length}}
#         {%for n, user in enumerate(users, 1)%}
#         {{n}}. {{user.name}} - должность: {{user.status}}
#         {%endfor%}
# """
#
# content["title"] = 'ЦИКЛ'
# content["users"] = []
# content["users"].append({"name": "Andrew", "status": "Worker"})
# content["enumerate"] = enumerate
# print(Template(tpl).render(content))

