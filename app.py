from flask import *
app = Flask(__name__)

application=app


@app.route("/")
def index():
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

@app.route("/create-order.html/")
def create_order():
    return render_template("create-order.html")

@app.route("/create-pay-invoice.html/")
def create_pay_invoice():
    return render_template("create-pay-invoice.html")

@app.route("/create-reminder.html/")
def create_reminder():
    return render_template("create-reminder.html")

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

@app.route("/create-ticket.html/")
def create_ticket():
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
