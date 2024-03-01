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
a.Multi_que(1,'if we want to tighten the axle lock what should we use?',('Allen key','axle','spanner','nuts and bolts'),'Allen key')
a.Multi_que_image(2,'Which part is this?','rc car.jpg',('castor wheel','normal wheel','nut','axle lock'),'castor wheel')
a.Multi_que(3,'what does the three wheel  car mostly relates to?',('truck','plane','rickshaw','bike'),'rickshaw')
a.Multi_que(4,"how many rectangular plates are needed for three wheel based model",("3","2","1","0"),"2")
a.Multi_que_image(5,'what is this called?','u-beam.jpg',('3.5 L-beam','7.5 U-beam','3.5 u-beam','u-channel'),'3.5 u-beam')
a.Multi_que(6,"THERE ARE FOUR WHEELS IN RC CAR 2 ARE CONNECTED WITH MOTORS AND TWO ARE CONNECTED IN FRONT WITH AXLE. WHAT IS THE NAME OF PART THAT CONNECTS BOTH THE AXLES?",("Axle coupler","Axle","Axle lock","filler"),"Axle coupler")
a.Multi_que_image(7,'WHERE WILL THE WIRE OF RIGHT MOTOR GETS ATTACHED?','brain.jpg',('M1','M2','M3','M4'),'M3')
a.Multi_que(8,"WE ARE INSERTING BRAIN ONTO WHICH PART?",("rectangular plate","u-channel","3.5 u-beam","u-beam"),"rectangular plate")
a.Multi_que_image(9,'WHAT IS THE NAME OF THIS PART?','filler.jpg',('filler','bolt','axle lock','nut'),'filler')
a.Multi_que_image(10,'WHAT IS THE NAME OF THIS PART AND WHERE CAN WE USE IT?','spanne.jpg',('spanner','allen key','axle','filler'),'spanner')
a.Multi_que(11,"Can castor wheel make good turns in car than normal wheel?",("true","false"),"true")
a.Multi_que_image(12,'WHICH PARTS ARE REQUIRED TO CREATE THIS PORTION?','model.jpg',('MOTOR,U-CHANNEL,FILLER,WHEEL,AXLE LOCK','SPANNER,U-CHANNEL,FILLER,WHEEL,AXLE LOCK','MOTOR,U-CHANNEL,FILLER,WHEEL,U-BEAM','MOTOR,U-CHANNEL,AXLE,WHEEL,AXLE LOCK'),'MOTOR,U-CHANNEL,FILLER,WHEEL,AXLE LOCK')
a.Multi_que(13,"CAN WE MOVE THE RC CAR IN EVERY DIRECTION (TRUE OR FALSE)?",("true","false"),"true")
a.Multi_que_image(14,"WHICH PART IS THIS?","3-hole connectore.png",("filler","nuts and bolts","3-hole connector","spanner"),"3-hole connector")
a.Multi_que(15,"ON WHICH PORT WILL THE WIRE OF TORQUE MOTOR GOES?",('M4','M3','M2','M1'),'M1')
a.Multi_que(16,"how many castor wheels are inserted in one-arm soccer bot",('1','2','3','4'),'1')
a.Multi_que_image(17,"WHICH PART IS THIS FROM MODEL?","L-beam.png",("l-channel","l-beam","u-channel","u-beam"),"l-beam")
a.Multi_que(18,"WHICH SIZE OF AXLE WE HAVE TO INSERT IN TORQUE MOTOR?",("5.5mm axle","7.5mm axle","3.5mm axle","none of these"),"3.5mm axle")
a.Multi_que(19,"Can we use castor wheel on the back of the model (true/false)?",("True","False"),"False")
a.Multi_que(20,"ON WHICH PART WE WILL INSERT THE ONE ARM ?",("square plate","rectangular plate",'u-channel','axle'),'rectangular plate')


a.get_answer()
a.show_answer()





