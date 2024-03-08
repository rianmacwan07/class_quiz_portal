# Multiple choice Questions
# Code snnipet and give output
# Question and give coding space to write code
# find the bugs and rewrite the code
import streamlit as sl
import pyperclip
import pandas as pd

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
        self.name = sl.text_input("", placeholder='Enter Your Name')
        sl.subheader("Age")
        age = sl.text_input('',placeholder="Enter You Age")
        sl.subheader("WhatsApp No.")
        whatsapp_no = sl.text_input('',placeholder="Enter Your WhatsApp No.")
        sl.subheader("School Name")
        school = sl.text_input("",placeholder='Enter Your School Name')
        sl.subheader("Class")
        s_class = sl.text_input('',placeholder="Enter Your Class")
        UserModule.result.update({"Name": self.name,'Age':age,"Whatsapp No":whatsapp_no,"School":school,'School Class':s_class})

    def Header(self):
        sl.subheader(f"Chapter : {self.chapter}")
        sl.subheader(f"Marks : {self.marks}")

    def Multi_que(self, q_num, question, options: tuple, ans):
        if 'disable' not in sl.session_state:
            state = sl.session_state['disable'] = 0
            self.state = state
        sl.markdown("---")
        sl.header(f"Question {q_num}: {question}")
        result = sl.radio('', options=options,key=q_num,disabled=sl.session_state['disable'])
        
        if sl.button("Submit",key=question):
            if result is None:
                pass
           
            elif result == ans:
                sl.success("Correct Answer")
                UserModule.corrct_ans += 1

            else:
                sl.warning("Wrong Answer")
                sl.success(f"Correct Answer: { ans}")
            self.state = 1
  
        UserModule.answer.update({question:ans})
        UserModule.result.update({question:result})

    def Multi_que_image(self, q_num, question, picture, options: tuple, ans):
        if 'disable' not in sl.session_state:
            state = sl.session_state['disable'] = 0
            self.state = state
        sl.markdown("---")
        sl.header(f"Question {q_num}: {question}")
        sl.image(f'{picture}',width = 300)
        result = sl.radio('', options=options,key=q_num,disabled=sl.session_state['disable'])
        
        if sl.button("Submit",key=question):
            if result is None:
                pass
           
            elif result == ans:
                sl.success("Correct Answer")
                UserModule.corrct_ans += 1

            else:
                sl.warning("Wrong Answer")
                sl.success(f"Correct Answer: { ans}")
            self.state = 1
  
        UserModule.answer.update({question:ans})
        UserModule.result.update({question:result})
    def code_snp(self, code, output, key):
        sl.markdown('---')
        sl.subheader("Give Output of Below snippet")
        sl.code(code, language=self.lang)
        st_output = sl.text_input("", placeholder="Output", key=key)
        if st_output == output:
            sl.success("Correct Answer")
            UserModule.corrct_ans += 1
        else:
            sl.warning("Wrong Answer")
            
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
        df.to_excel(f'{self.name} response.xlsx')
        return UserModule.result
    
    def show_answer(self):
        sl.write("See correct Answers:")
        sl.table(UserModule.answer)

a = UserModule('chapters','marks','lang')
a.student_info()
a.Header()
a.Multi_que(1,'IS SOCCER BOT A THREE WHEEL BASED OR FOUR WHEEL BASED MODEL?',('True','False'),'True')
a.Multi_que_image(2,'WHICH PART IS THIS?','3-hole connectore.jpg',('bolts','axle lock','3-hole connector','filler'),'3-hole connector')
a.Multi_que(3,'DO WE NEED CASTOR WHEEL TO MAKE ONE-ARM SOCCER BOT (TRUE/FALSE)?',('True','False'),'True')
a.Multi_que_image(4,"WHAT IS THE NAME OF THIS MOTOR?","motor.png",("high speed ","generator motor","torque","slow speed"),"torque")
a.Multi_que(5,'ON WHICH PORT WILL THE WIRE OF TORQUE MOTOR GOES?',('M2','M1','M3','M4'),'M1')
a.Multi_que(6,"ON WHICH PART WE WILL INSERT THE ONE ARM?",("D-PLATE",'SQUARE PLATE','RECTANGULAR PLATE','U-PLATE'),"RECTANGULAR PLATE")
a.Multi_que_image(7,"WHAT IS THE NAME OF THIS PART?","square_plate.png",("square plate","rectangular plate","d-plate","m-plate"),"square plate")
a.Multi_que_image(8,'IDENTIFY THIS PART?','L-beam.png',('SQUARE PLATE','l-beam','RECTANGULAR PLATE','U-CHANNEL'),'l-beam')
a.Multi_que(9,"WHAT DO WE HAVE TO INSERT IN BEFORE INSERTING THREE-HOLE CONNECTOR?",("bolt","nut","axle",'filler'),"filler")
a.Multi_que(10,"WHICH SIZE OF AXLE WE HAVE TO INSERT IN TORQUE MOTOR?",("5.5mm","12.5mm",'3.5mm','7.5mm'),'3.5mm')
a.Multi_que(11,"FROM WHICH TO WHICH DIRECTION WE CAN MOVE THE SOCCER BOT ARM?",('RIGHT TO LEFT','ONLY LEFT','BOTTOM TO UP','ONLY UP'),'RIGHT TO LEFT')
a.Multi_que(12,"DO WE NEED BOTH THE REMOTE BUTTON TO CONTROL ONE ARM SOCCER BOT?",("True","False"),"True")

a.get_answer()
a.show_answer()





