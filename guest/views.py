from flask import Blueprint,render_template,request,url_for,redirect

view = Blueprint("view",__name__,static_folder="static", template_folder="templates")

#------Developer registrations----------------#
@view.route("/dev_register",methods = ['GET'])
def dev_register():
    """Registration PAGE FOR DEVELOPERS"""
    return render_template('Register.html')
#----------------------------------------#
@view.route('/charts',methods=['GET'])
def charts():
    """Demo of google charts on static data"""
    if request.method == 'GET':
        return render_template('gcharts.html')
#----------------------------------------#
@view.route('/devsr',methods=['GET']) #Serves form template for password request
def request_form():
    return render_template('dev_services.html')
