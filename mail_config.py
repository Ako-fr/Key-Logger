import smtplib, ssl

def sendEmail(logs):
	smtp_server = "smtp.gmail.com"
	port = 587 
	email_message = "Ici" # Definissez l'adresse qui enverra les logs
	mdp = "Ici" # Indiquez le mot de passe du compte qui compte envoyé les logs
	logs_email = "Ici" # Definissez l'adresse qui recevra l'email contenant les logs

	context = ssl.create_default_context()

	try:
	    server = smtplib.SMTP(smtp_server,port)
	    server.ehlo() 
	    server.starttls(context=context) 
	    server.ehlo()
	    server.login(email_message, mdp)
	    server.sendmail(email_message, logs_email, logs)
	   
	except Exception as e:
	    print(e)
	finally:
	    server.quit()
