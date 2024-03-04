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
a.Multi_que(1,'IF WE WANT TO TIGHTEN THE AXLE LOCK WHAT SHOULD BE USE?',('BOLTS','SPANNER','ALLEN KEY','NUTS'),'ALLEN KEY')
a.Multi_que_image(2,'WHERE WILL THE WIRE OF RIGHT MOTOR GETS ATTACHED?','brain.jpg',('M4','M1','M2','M3'),'M3')
a.Multi_que(3,'THERE ARE FOUR WHEELS IN RC CAR 2 ARE CONNECTED WITH MOTORS AND TWO ARE CONNECTED IN FRONT WITH AXLE. WHAT IS THE NAME OF PART THAT CONNECTS BOTH THE AXLES?',('AXLE','AXLE COUPLER','COUPLER','3.5 MM AXLE'),'AXLE COUPLER')
a.Multi_que(4,"THE RECTANGULAR PLATE WILL BE JOINED TO 2 OF THE U-CHANNEL AFTER HOW MANY HOLES?",("4TH","5TH","6TH","3RD"),"4TH")
a.Multi_que_image(5,'WHAT IS THE NAME OF THIS PART?','filler.jpg',('bolts','filler','nuts','axle lock'),'3.5 u-beam')
a.Multi_que(6,"CAN WE MOVE THE RC CAR IN EVERY DIRECTION (TRUE OR FALSE)?",("TRUE",'FALSE'),"TRUE")
a.Multi_que(7,"IN WHICH PORT WILL THE LEFT MOTOR WIRE GO??",("M2","M1","M3","M2"),"M4")
a.Multi_que_image(8,'IDENTIFY THIS PART?','rectangular.png',('SQUARE PLATE','D-PLATE','RECTANGULAR PLATE','U-CHANNEL'),'u-beam')
a.Multi_que(9,"WE ARE INSERTING BRAIN ONTO WHICH PART?",("U-CHANNEL","D-PLATE","RECTANGULAR PLATE",'U-BEAM'),"RECTAGULAR")
a.Multi_que(10,"ARE WE INSERTING ANY WIRE ON THE S1,S2,S3,S4,S5 PORT (TRUE/FALSE)?",("True","False"),'False')
a.Multi_que(11,"WHICH WHEELS ARE GIVING THE DIRECTION TO WHOLE RC CAR?",('CASTOR WHEEL','FRONT WHEEL','BACK WHEEL','SINGLE WHEEL'),'FRONT WHEEL')
a.Multi_que_image(12,"WHAT IS THE NAME OF THIS PART","axle_lock.jpg",("axle","axle coupler","axle lock","filler"),"axle lock")
a.Multi_que(13,"HOW MANY AXLES CAN BE INSTALLED IN AXLE LOCK?",("3","1","4","2"),"1")
a.Multi_que(14,"CAN WE USE ALLEN KEY TO TIGHTEN BOLTS AND NUTS (TRUE/FALSE)?",("True",'False'),"True")
a.Multi_que_image(15,"IS THIS PART USED IN RC CAR?","d-plate.png",("True","False"),"True")
a.Multi_que(16,"WHICH SIZE AXLE IS USED IN MODEL FOR BACK WHEELS?",("3.5mm","5.5mm","7.5mm","12.5mm"),"3.5mm")
a.get_answer()
a.show_answer()





