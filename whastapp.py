#pip install pywhatkit 
#pip install flask
import pywhatkit 

# Usamos Un try-except
try: 

  # Enviamos el mensaje

  pywhatkit.sendwhatmsg("+57numero",  
                        "Mami te quiero mucho",
                        17,33) 

  print("Mensaje Enviado") 

  

except: 
  print("Ocurrio Un Error")
