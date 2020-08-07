from flask import *
app = Flask(__name__)
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import re
import os
application=app
from datetime import datetime
import sqlite3
from werkzeug.utils import secure_filename

db_path = "HulkPage.db"


UPLOAD_FOLDER = 'uploads'
app.secret_key = 'roKBFeMEysoxUPUzVx7cRC17eUwEpJEWvxS9K7Gn'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pythonlogin'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# Intialize MySQL
#connects it to the books-collection database


#creates the cursor


#execute the query which creates the table called books with id and name
#as the columns

#executes the query which inserts values in the table


#commits the executions


@app.route('/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        db = mysql.connector.connect(user='root', database='pythonlogin')
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('index'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('pages-login.html', msg='')

@app.route("/create-transaction/")
def create_transaction():
    id=5
    client=request.args.get("client")
    service=request.args.get("service")
    service_group_id=request.args.get("service_group_id")
    service_group=request.args.get("service_group")
    created_at=str(datetime.now())
    renewal=str(datetime.now())
    amount=request.args.get("amount")
    status="Active"
    try:
        if not Transaction.get(id):
            conn = sqlite3.connect('HulkPage.db')
            c = conn.cursor()
            c.execute("INSERT INTO transactions (id,client,service,service_group,service_group_id,created_at,renewal,amount,status) VALUES (?, ?,?,?,?,?,?,?,?)", (id,client,service,service_group,service_group_id,created_at,renewal,amount,status))
            conn.commit()

                #closes the connection
            conn.close()
            return jsonify({"success":True,"message":"Transaction Created"})
    except:
        return jsonify({"success":False,"message":"Error while Creating Transaction please check inputs"})






@app.route("/index/")
def index():
    db_connection = sqlite3.connect(db_path)
    cursor = db_connection.cursor()
    current_day = datetime.now().day
    return render_template("index2.html")

@app.route("/active-order.html/")
def active_order():
    return render_template("active-order.html")

@app.route("/activity-log.html/")
def activity_log():
    return render_template("activity-log.html")

@app.route("/add-language.html/")
def add_language():
    return render_template("add-language.html")

@app.route("/add-new-page.html/")
def add_new_page():
    return render_template("add-new-page.html")

@app.route("/add-news-announcement.html/")
def add_news_announcement():
    return render_template("add-news-announcement.html")

@app.route("/addons-order.html/")
def addons_order():
    return render_template("addons-order.html")

@app.route("/addons.html/")
def addons():
    return render_template("addons.html")

@app.route("/affiliate.html/")
def affiliate():
    return render_template("affiliate.html")

@app.route("/agreement.html/")
def agreement():
    return render_template("agreement.html")

@app.route("/blog.html/")
def blog():
    return render_template("blog.html")

@app.route("/browse-invoice.html/")
def browse_invoice():
    return render_template("browse-invoice.html")

@app.route("/browse-order.html/")
def browse_order():
    return render_template("browse-order.html")

@app.route("/browse-language.html/")
def browse_language():
    return render_template("browse-language.html")

@app.route("/bulk-mail.html/")
def bulk_mail():
    return render_template("bulk-mail.html")

@app.route("/bulk-sms.html/")
def bulk_sms():
    return render_template("bulk-sms.html")

@app.route("/cancel_request-order.html/")
def cancel_request_order():
    return render_template("cancel_request-order.html")

@app.route("/cancelled-invoice.html/")
def cancelled_invoice():
    return render_template("cancelled-invoice.html")

@app.route("/cancelled-order.html/")
def cancelled_order():
    return render_template("cancelled-order.html")

@app.route("/cash-management.html/")
def cash_management():
    return render_template("cash-management.html")

@app.route("/categories-create.html/")
def categories_create():
    return render_template("categories-create.html")

@app.route("/categories.html/")
def categories():
    return render_template("categories.html")

@app.route("/client-testimonial.html/")
def client_testimonial():
    return render_template("client-testimonial.html")

@app.route("/contact-message.html/")
def contact_message():
    return render_template("contact-message.html")

@app.route("/create-article.html/")
def create_article():
    return render_template("create-article.html")

@app.route("/create-blog.html/")
def create_blog():
    return render_template("create-blog.html")

@app.route("/create-custom-field.html/")
def create_custom_field():
    return render_template("create-custom-field.html")

@app.route("/create-feedback.html/")
def create_feedback():
    return render_template("create-feedback.html")


@app.route("/create-order.html/", methods=['GET', 'POST'])
def create_order():
    conn = sqlite3.connect('HulkPage.db')
    c = conn.cursor()
    message=''
    if request.method == 'POST' and 'amount' in request.form and 'client' in request.form:
        id=37
        client=request.form['client']
        service_group=request.form['service_group']
        service_group_id=37
        service=request.form['service']
        duration=request.form['duration']
        amount=request.form['amount']
        created_at=str(datetime.now())
        renewal=str(datetime.now())
        status="Active"
        cursor.execute("SELECT * FROM orders WHERE id=%s", (id,))
        order_Id= cursor.fetchone()
        if not order_id:
            c.execute("INSERT INTO orders (id,client,service,service_group,service_group_id,created_at,renewal,amount,status) VALUES (?, ?,?,?,?,?,?,?,?)", (id,client,service,service_group,service_group_id,created_at,renewal,amount,status))
            conn.commit()

        #closes the connection
            conn.close()
            return redirect(url_for('create_order'))
            message="Created Order"

        else:
            message="Already Exists"


    return render_template("create-order.html",message=message)



@app.route("/create-pay-invoice.html/")
def create_pay_invoice():
    conn = sqlite3.connect('HulkPage.db')
    c = conn.cursor()
    message=''
    if request.method == 'POST' and 'amount' in request.form and 'client' in request.form:
        id=37
        client=request.form['client']
        amount=request.form['amount']
        description=request.form['description']
        tax_type=request.form['tax_type']
        tax_exempt=request.form['tax_exempt']
        last_pay=request.form['last_date']
        create_date=str(datetime.now())
        paid=request.form["paid"]
        unpaid=request.form["unpaid"]
        if paid:
            status=paid
        else:
            status=unpaid
        c.execute("INSERT INTO payinvoices (id,client,amount,description,tax_type,tax_exempt,last_pay,create_date,amount,status) VALUES (?, ?,?,?,?,?,?,?,?,?)", (id,client,amount,description,tax_type,tax_exempt,last_pay,create_date,amount,status))
        conn.commit()

        #closes the connection
        conn.close()
        return redirect(url_for('create_pay_invoice'))
        message="Created Invoice"


    return render_template("create-pay-invoice.html",message=message)

@app.route("/create-reminder.html/")
def create_reminder():
    conn = sqlite3.connect('HulkPage.db')
    c = conn.cursor()
    message=''
    if request.method == 'POST' and 'amount' in request.form and 'client' in request.form:
        id=37
        text=request.form['text']
        period=request.form['period']
        time=requests.form['time']
        status="Active"
        c.execute("INSERT INTO reminders (id,text,period,time,status) VALUES (?, ?,?,?,?,?,?,?,?)", (id,text,period,time,status))
        conn.commit()

        #closes the connection
        conn.close()
        return redirect(url_for('create_order'))
        message="Created Reminder"
    return render_template("create-reminder.html",message=message)

@app.route("/create-response.html/")
def create_response():
    return render_template("create-response.html")

@app.route("/create-service-group.html/")
def create_service_group():
    return render_template("create-service-group.html")

@app.route("/create-slider.html/")
def create_slider():
    return render_template("create-slider.html")

@app.route("/create-task-plan.html/")
def create_task_plan():
    return render_template("create-task-plan.html")

@app.route("/create-ticket.html/", methods=['GET', 'POST'])
def create_ticket():
    conn = sqlite3.connect('HulkPage.db')
    c = conn.cursor()
    message=''
    if request.method == 'POST':
        id=37
        topic=request.form['topic']
        department=request.form['department']
        staff=request.form['staff']
        file=request.files['file']
        file.save(secure_filename(file.filename))
        file_name=file.filename
        create_date=str(datetime.now())
        status="Active"
        service=request.form['service']
        first=request.form['response']
        second=request.form['area']
        if first:
            response=first
        else:
            response=second
        priority=request.form['priority']
        c.execute("INSERT INTO tickets (id,topic,department,staff,file,create_date,status,service,response) VALUES (?,?,?,?,?,?,?,?,?)", (id,topic,department,staff,file_name,create_date,status,service,response))
        conn.commit()

        #closes the connection
        conn.close()
        return redirect(url_for('create_ticket'))
        message="Created Invoice"

    return render_template("create-ticket.html")

@app.route("/custom-fields.html/")
def custom_fields():
    return render_template("custom-fields.html")

@app.route("/customer.html/")
def customer():
    return render_template("customer.html")

@app.route("/detail-invoice.html/")
def detail_invoice():
    return render_template("detail-invoice.html")

@app.route("/document-filter.html/")
def document_filter():
    return render_template("document-filter.html")

@app.route("/document-records.html/")
def document_records():
    return render_template("document-records.html")

@app.route("/find-replcae.html/")
def find_replace():
    return render_template("find-replace.html")

@app.route("/formalized-invoice.html/")
def formalized_invoice():
    return render_template("formalized-invoice.html")

@app.route("/knowledge-base.html/")
def knowledge_base():
    return render_template("knowledge-base.html")

@app.route("/knowledgebase-categories-create.html/")
def knowledgebase_categories_create():
    return render_template("knowledgebase-categories-create.html")

@app.route("/knowledgebase-categories.html/")
def knowledgebase_categories():
    return render_template("knowledgebase-categories.html")

@app.route("/module-activity-log.html/")
def module_activity_log():
    return render_template("module-activity-log.html")

@app.route("/module-setting.html/")
def module_setting():
    return render_template("module-setting.html")

@app.route("/news.html/")
def news():
    return render_template("news.html")

@app.route("/non-formalized-invoice.html/")
def non_formalized_invoice():
    return render_template("non-formalized-invoice.html")

@app.route("/order-details.html/")
def order_details():
    return render_template("order-details.html")

@app.route("/pages-login.html/")
def admin_login():
    return render_template("pages-login.html")

@app.route("/pages.html/")
def pages():
    return render_template("pages.html")

@app.route("/paid-invoice.html/")
def paid_invoice():
    return render_template("paid-invoice.html")

@app.route("/pending-order.html/")
def pending_order():
    return render_template("pending_order.html")

@app.route("/product-addons.html/")
def product_addons():
    return render_template("product-addons.html")

@app.route("/reference-category-create.html/")
def reference_category_create():
    return render_template("reference-category-create.html")

@app.route("/reference-category.html/")
def reference_category():
    return render_template("reference-category.html")

@app.route("/references.html/")
def references():
    return render_template("references.html")

@app.route("/reminder.html/")
def reminder():
    return render_template("reminder.html")

@app.route("/reseller.html/")
def reseller():
    return render_template("reseller.html")

@app.route("/response-categories.html/")
def response_categories():
    return render_template("response-categories.html")

@app.route("/responses.html/")
def responses():
    return render_template("responses.html")

@app.route("/session-logs.html/")
def session_logs():
    return render_template("session-logs.html")

@app.route("/slider-list.html/")
def slider_list():
    return render_template("slider-list.html")

@app.route("/suspended-order.html/")
def suspended_order():
    return render_template("suspended-order.html")

@app.route("/systemic-error-log.html/")
def systemic_error_log():
    return render_template("systemic-error-log.html")

@app.route("/systemic-sms-record.html/")
def systemic_sms_record():
    return render_template("systemic-sms-record.html")

@app.route("/systemic-mail-records.html/")
def systemic_mail_record():
    return render_template("systemic-mail-records.html")

@app.route("/task-planner.html/")
def task_planner():
    return render_template("task-planner.html")

@app.route("/ticket-details.html/")
def ticket_details():
    return render_template("ticket-details.html")

@app.route("/tickets.html/")
def tickets():
    return render_template("tickets.html")

@app.route("/unpaid-invoice.html/")
def unpaid_invoice():
    return render_template("unpaid-invoice.html")

@app.route("/upgrade_downgrade-order.html/")
def upgrade_downgrade_order():
    return render_template("upgrade-downgrade-order.html")

@app.route("/wf-fraud.html/")
def wf_fraud():
    return render_template("wf-fraud.html")


if __name__ == "__main__":
    app.run(debug=True)
