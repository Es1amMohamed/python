from shlex import quote
from turtle import back
import qrcode
import image
a = 0
while True:
    a+=1
    qr = qrcode.QRCode(
        version  = 15,
        box_size = 10,
        border   = 5,
        
    )
    code = input(' Enter your code ').strip()
    try: 
        

        data = code
        qr.add_data(data)
        qr.make(fit = True )
        img = qr.make_image(fill = 'black', back_color = 'white' )
        img.save('test{}.png'.format(a))
        again= input(" Do you Want To Create Another QRcobe Y or N ? ").capitalize().strip()
        if again == 'N' :
            break
    except :
        pass