import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# E-Mail-Konfiguration
sender_email = 'hinoran.marlon@gmail.com'
receiver_email = 'marlon.profils@gmail.com'
password = 'lmbd jiyu grnj vdox'

# HTML-Inhalt des Newsletters
html_content = """
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Newsletter Test</title>
</head>
<body>
  <table width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr>
      <td align="center">
        <img src="https://example.com/bild.jpg" alt="Bild" style="max-width: 100%;">
      </td>
    </tr>
    <tr>
      <td align="center" style="padding: 20px;">
        <h1 style="font-size: 24px; color: #333333;">werbung</h1>
        <p style="font-size: 16px; color: #666666;">werbung. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
      </td>
    </tr>
  </table>
</body>
</html>
"""

# E-Mail-Vorbereitung
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = 'Test Newsletter'

# HTML-Inhalt als MIMEText hinzufügen
msg.attach(MIMEText(html_content, 'html'))

# E-Mail-Versand
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail SMTP-Server und Port
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print('E-Mail wurde erfolgreich gesendet!')
except Exception as e:
    print(f'Fehler beim Senden der E-Mail: {e}')
finally:
    server.quit()
