# Multiple choice Questions
# Code snnipet and give output
# Question and give coding space to write code
# find the bugs and rewrite the code
import streamlit as sl
import pyperclip
import pandas as pd
import random
sl.set_page_config(page_title="Geniusmart Exam Portal", page_icon=':book:')
sl.markdown(' <h1 style="text-align:center">Geniusmart Academy</h1> ',
            unsafe_allow_html=True)
                                                
class UserModule:
    corrct_ans = 0
    result = {}
    answer = {}
    mcq_question = []
    mcq_answer = []

    def __init__(self, chapter: str, marks: str, lang: str) -> None:
        
        self.chapter = chapter
        self.marks = marks
        self.lang = lang

    def student_info(self):
        sl.markdown("---")
        sl.subheader("Student Name")
        name = sl.text_input("", placeholder='Enter Your Name')
        sl.subheader("Age")
        age = sl.text_input('',placeholder="Enter You Age")
        sl.subheader("WhatsApp No.")
        whatsapp_no = sl.text_input('',placeholder="Enter Your WhatsApp No.")
        sl.subheader("School Name")
        school = sl.text_input("",placeholder='Enter Your School Name')
        sl.subheader("Class")
        s_class = sl.text_input('',placeholder="Enter Your Class")
        UserModule.result.update({"Name": name,'Age':age,"Whatsapp No":whatsapp_no,"School":school,'School Class':s_class})

    def Header(self):
        sl.subheader(f"Chapter : {self.chapter}")
        sl.subheader(f"Marks : {self.marks}")

    def Multi_que(self, q_num, question, options: tuple, ans):
        sl.markdown("---")
        sl.header(f"Question {q_num}: {question}")
        result = sl.radio('', options=options,key=q_num,index=None)
        if result == ans:
            sl.write(1)
            UserModule.corrct_ans += 1
            
        else:
            sl.write(0)
        UserModule.answer.update({question:ans})
        UserModule.result.update({question:result})

    def code_snp(self, code, output, key):
        sl.markdown('---')
        sl.subheader("Give Output of Below snippet")
        sl.code(code, language=self.lang)
        st_output = sl.text_input("", placeholder="Output", key=key)
        if st_output == output:
            UserModule.corrct_ans += 1
            sl.write(UserModule.corrct_ans)
        UserModule.result.update({code: st_output})
        UserModule.answer.update({code:output})

    def code_que(self, question, q_num,key):
        sl.markdown("---")
        sl.header(f"Question {q_num}:")
        sl.subheader(f"{question}")
        st_code = sl.text_area(label="Write Code Here!",key=key)
        UserModule.result.update({question: st_code})

    def find_bug_err(self, code,key):
        sl.markdown("---")
        sl.subheader("Solve The Below Code !!!")
        sl.code(code, language= self.lang)

        def copying():
            pyperclip.copy(code)
        copy = sl.button("Copy Code", on_click=copying,key=key)
        if copy:
            sl.write('Code Copied!')
        workspace = sl.text_area('Paste Your code here!',key=key+1)
        UserModule.result.update(
            {'Find Bug/Error Question': code, 'Find Bug/Error Answer': workspace})

    def get_answer(self):
        sl.success(f"Obtained Marks: {UserModule.corrct_ans}")
        df = pd.DataFrame(data=UserModule.result,index=["Answer"])
        df = (df.T)
        df.to_excel('response.xlsx')
        return UserModule.result
    
    # def get_manual_que(self):
    #     list = []
    #     question = sl.text_input("Enter your Question:",key=1)
    #     option = sl.text_input('Enter your Options:',key=2)
    #     answer = sl.text_input('Enter your Answer:',key=3)
    #     add_question = sl.button("Add Question",key=4)
    #     if add_question:
    #        list.append({'question':question,'option':option.split(','),'Ans':answer})
    #     submit = sl.button("Submit Questions",key=5)
    #     if submit:
    #        return list

    def get_manual_ans(self):
        # num = sl.number_input("How many questions do you want to add:")
        list = []
        i = 1
    
        question = sl.text_input(f"Enter your Question NO. {i}:",key=random.randint(1,100))
        option = sl.text_input('Enter your Options:',key=random.randint(101,200))
        answer = sl.text_input('Enter your Answer:',key=random.randint(201,300))
        list.append({'question':question,'option':option.split(','),'Ans':answer})
        i+=1
        print(i)
        return list 

    
    def show_answer(self):
        sl.table(UserModule.answer)





