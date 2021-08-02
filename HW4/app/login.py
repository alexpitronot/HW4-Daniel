import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['post', 'get'])


def login():
    message = ''
    if request.method == 'POST':
        fname = request.form.get('First-Name:')  # access the data inside 
        lname = request.form.get('Last-Name:')
        smoking = request.formt.get('Is_Smoking:')
        id = request.formt.get('ID:')
        birthday = request.form.get('Birthday:')

        # validifiction
        worklist = {
    1 : {},
    2 : {},
    3 : {}
}
        for x in range(3):
            fname  = (input("What is your First name? : "))
            FC = fname[0].upper()
            if fname[0]!=FC:
               a = fname[1:]
               fname=("{}"+a).format(FC)

            lname = str(input("What is your Last Name? :"))
            FD = lname[0].upper()
            if lname[0]!=FD:    
               c = lname[1:]
               lname = ("{}"+c).format(FD)

            smoking = bool(input("If you are smoking, enter \'Y\', if not - continue without input: "))
            
            id = str(input("what is yor ID? :"))
            while len(id)>9:
               print("ID must be up to 9 digits")
               id = input("what is your ID? : ")
            while len(id)<9:
               id = "0" + id
            
            error = 1
            while error == 1:
                birthday = input("What is your B'day? (in DD/MM/YYYY) :")
                try:
                    datetime.datetime.strptime(birthday, "%d/%m/%Y")
                    error = 0
                except ValueError:
                    print("Wrong format! It should be DD/MM/YYYY. Try again")
                    error = 1
            birthdate = datetime.datetime.strptime(birthday,"%d/%m/%Y").date() 
            birthday = birthdate.strftime('%d/%B/%Y')
           
            file1=open("data.txt","w")
            text=fname+lname+smoking+id+birthday
            file1.write(text)
            file1.close()

        return render_template('login.html',message=message,fname=fname,lname=lname,smoking=smoking,id=id,birthday=birthday)
    return render_template('login.html')    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True) 