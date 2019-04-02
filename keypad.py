#   Demonstrates a number of PySimpleGUI features including:      
#   Default element size      
#   auto_size_buttons      
#   Button      
#   Dictionary return values      
#   Update of elements in window (Text, Input)    
#   do_not_clear of Input elements

import PySimpleGUI as sg

image_on = './Buttons/on.png'
image_off = './Buttons/off.png'
background = '#d9d9d9'

state_battery = False
state_armed = False

layout = [[sg.Input(size=(20, 1), do_not_clear=True, justification='right', key='input')],
          [sg.Text('Modo 0', size=(10, 1), font=('Helvetica', 18), text_color='red'),sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('ESC')],      
          [sg.Text('Modo 1', size=(10, 1), font=('Helvetica', 18), text_color='red'),sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('ENTER')],      
          [sg.Text('Battery', size=(10, 1), font=('Helvetica', 18), text_color='red'),sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('PANIC')],      
          [sg.Text('Error', size=(10, 1), font=('Helvetica', 18), text_color='red'),sg.Button('*'), sg.Button('0'), sg.Button('#'), sg.Button('SOS')],      
          #[sg.Checkbox('Battery', default=True,key='Battery',disabled = True), sg.Checkbox('Armed', default=True,key='Armed'),sg.Text('LOG:'),sg.Text('', size=(20,1), key='out')],
          [sg.Button('Battery', button_color=('black',background),image_filename=image_off, image_size=(50, 50), image_subsample=2, border_width=0, key='Battery'),sg.Button('Armed', button_color=('black','#d9d9d9'),image_filename=image_off, image_size=(50, 50), image_subsample=2, border_width=0, key='Armed'),sg.Text('LOG:'),sg.Text('', size=(20,1), key='out')],
          ]

           

window = sg.Window('Keypad', default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=False).Layout(layout)

def toggle_LED(led_name):  
  if (led_name=='Battery'):     
      window.FindElement(led_name).Update(button_color=('white', 'black'))
  elif (led_name=='Armed'):     
      window.FindElement(led_name).Update(button_color=('white', 'black'))
  
# Loop forever reading the window's values, updating the Input field    
keys_entered = ''      
while True:      
    event, values = window.Read()  # read the window    
    if event is None:  # if the X button clicked, just exit
      break      
    if event == 'ESC':  # clear keys if clear button      
      keys_entered = ''     
      window.FindElement('out').Update('')      
    elif event in '#*1234567890':      
      keys_entered = values['input']  # get what's been entered so far      
      keys_entered += event  # add the new digit      
    elif event == 'ENTER':      
      keys_entered = values['input']      
      window.FindElement('out').Update(keys_entered)  # output the final string    
    elif event == 'PANIC':            
      window.FindElement('out').Update(keys_entered) 
    elif event == 'SOS':            
      window.FindElement('out').Update(keys_entered)       
    elif event == 'Battery' :             
      ret = window.FindElement('Battery').GetText()
      if(ret=='Battery'):
        window.FindElement('Battery').Update(' Battery ',image_filename=image_on, image_size=(50, 50), image_subsample=2)
      elif(ret==' Battery '):
        window.FindElement('Battery').Update('Battery',image_filename=image_off, image_size=(50, 50), image_subsample=2)

    elif event == 'Armed' : 
        ret = window.FindElement('Armed').GetText()            
        if(ret=='Armed'):
          window.FindElement('Armed').Update(' Armed ',image_filename=image_on, image_size=(50, 50), image_subsample=2)
        elif(ret==' Armed '):
          window.FindElement('Armed').Update('Armed',image_filename=image_off, image_size=(50, 50), image_subsample=2)
      


    window.FindElement('input').Update(keys_entered)  # change the window to reflect current key string