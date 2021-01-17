import streamlit as st
from program import pre

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


local_css("style.css")
st.markdown("""<div class='ripple-background'>
  <div class='circle xxlarge shade1'></div>
  <div class='circle xlarge shade2'></div>
  <div class='circle large shade3'></div>
  <div class='circle mediun shade4'></div>
  <div class='circle small shade5'></div>
</div>
""", unsafe_allow_html=True)
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
# import base64
#
#
# @st.cache(allow_output_mutation=True)
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()
#
#
# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
#
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return
#
#
# set_png_as_page_bg('background.png')

st.title('Chương trình phân loại văn bản tự động')
article = st.text_area("Nhập văn bản", height=300)
if st.button('Enter'):
    if not article.strip():
        st.warning('Chưa có văn bản nào đưuọc nhập!!')
        st.stop()
    category, proba = pre(article)
    st.markdown("<b>Văn bản này thuộc về thể loại {}</b>".format(category), unsafe_allow_html=True)
    st.markdown("<b>Độ tin cậy: {} % </b>".format(proba), unsafe_allow_html=True)



