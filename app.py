import os
import google.generativeai as genai
import streamlit as st
from pdfextractor import text_extractor
from wordextractor import doc_text_extractor
from image2text import extract_text_image

# lets configure the genai model
gemini_key=os.getenv('Gemini API Key2')
genai.configure(api_key=gemini_key)
model=genai.GenerativeModel('gemini-2.5-flash-lite',
                            generation_config={
                                'temperature':0.5
                            })

# lets create the sidebar
st.sidebar.title('UPLOAD YOUR NOTES:- ')
st.sidebar.subheader('Only upload the images ,PDF and DOCX')
user_file= st.sidebar.file_uploader('Upload Here:',type=['pdf','docx','jpg','jpeg','jiif'])

if user_file:
   st.sidebar.success('File Uploaded Successfully')
   if user_file.type=='application/pdf': 
      user_text= text_extractor(user_file)

   elif user_file.type in ['image/png','image/jpg','image/jpeg','image/jfif']:
        user_text=extract_text_image(user_file)
   elif user_file.type =='application/vnd.openxmlformats-officedocument.wordprocessingml':
        user_text=doc_text_extractor(user_file) 
   else:
       st.sidebar.error('Enter the correct file type')         
    
    # lets create the main pages

st.title(':orange[MOM Generator:-] :blue[AI Assisted Minutes of Meeting Generator.]')
st.subheader(':violet[This application creates generalized minutes of meeting from ]')
st.write('''
Follow the steps:
1.Upload the notes in PDF,DOCX or Image format in sidebar.
2.Click "generate" to generate the MOM.''')

if st.button('Generate'):
    with st.spinner("Please Wait....."):
        prompt =f'''
        <Role> You are an expert in writing and formating minutes of meetings.
        <Goal> Create minutes of meetings from the notes that user has provided.
        <Context> The user has provided some rough notes as text..Here are the notes:-
        <Format> The Output must follow the below format.
        * Title: Assume title of the meeting.
        * Agenda: Assume agenda of the meeting.
        * Attendees: Name of the attendees (If the name of the attendees is not there keep it NA )
        * Date and Place: date and the place of the meeting(if not provided keep it Online.)
        * Body> The body should follow the following sequence of points.
            * Mention Key points discussed.
            * Highlight and decision that hass been followed.
            * Mention Actionable Items.
            * Mention any deadline if discussed
            * add a 2-3 line of summary.

        <Instruction>
        * Use the bullet points and highlight the important keywords by making them hold.
        * Generate the output in docs format
        '''
    response=model.generate_content(prompt)
    st.write(response.text)

    if st.download_button(label='Download',
                       data=response.text,
                       file_name='mom_generated.text',
                       mime='text/plain'):
         st.success('Your file has been downloaded successfully')

#streamlit
#google.generativeai
#pypdf
#opencv-python-headless
##python-docx
#pillow