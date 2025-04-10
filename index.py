import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)

@app.route("/")
def index():
	homepage = "<h1>王珮淳Python網頁</h1>"
	homepage += "<a href=/mis>MIS</a><br>"
	homepage += "<a href=/today>顯示日期時間</a><br>"
	homepage += "<a href=/welcome?nick=王珮淳&work=pu>傳送使用者暱稱</a><br>"
	homepage += "<a href=/account>網頁表單傳值</a><br>"
	homepage += "<a href=/about>王珮淳簡介網頁</a><br>"
	homepage += "<br><a href=/read>讀取Firestore資料</a><br>"
	return homepage	

@app.route("/mis")
def mis():
	return "<h1>王珮淳</h1>"	

@app.route("/today")
def today():
	tz = timezone(timedelta(hours=+8))
	now = datetime.now(tz)
	return render_template("today.html", datetime = str(now))

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/welcome", methods=["GET"])
def welcome():
	user = request.values.get("nick")
	w = request.values.get("work")
	return render_template("welcome.html", name=user, work = w)

@app.route("/account", methods=["GET", "POST"])
def account():
	if request.method == "POST":
		user = request.form["user"]
		pwd = request.form["pwd"]
		result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd
		return result

	else:
		return render_template("account.html")
		
@app.route("/read")
def read():
    Result = ""
    db = firestore.client()
    collection_ref = db.collection("靜宜資管")    
    docs = collection_ref.get()    
    for doc in docs:         
        Result += "文件內容：{}".format(doc.to_dict()) + "<br>"    
    return Result

if __name__ == "__main__":
	app.run()