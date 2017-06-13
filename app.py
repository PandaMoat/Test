#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response
import json
import dpctl

ovsclient = Flask(__name__)

@ovsclient.route('/ovs/showdp/<string:dp>', methods=['GET'])
def get_dps(dp):
    if dp not in dpctl.dump_dps():
        return 'Datapath Does Not Exist'
    else:
        return dpctl.show(dp)
 
@ovsclient.errorhandler(404)
def not_found(error):
    return make_response(jsonify('Not Found'), 404)

@ovsclient.errorhandler(400)
def bad_request(error):
    return make_response(jsonify('Bad Request'), 400)

@ovsclient.route('/ovs/createpath/<dp>', methods=['GET', 'POST'])
def create_datapath(dp):
    
    if dp not in dpctl.dump_dps():
       dpctl.add_dp(dp)
       return 'Success!'
    else:
       return 'DataPath Already Exists'
    
    

@ovsclient.route('/ovs/deletepath/<dp>', methods=['GET', 'DELETE'])
def delete_datapath(dp):
    
    if dp not in dpctl.dump_dps():
        return 'Datapath Does Not Exist'
    else:
        dpctl.del_dp(dp)
        return 'Deleted'

@ovsclient.route('/ovs/addif/<dp>/<netdev>', methods=['GET', 'POST'])
def add_if(dp, netdev):
    if dp in dpctl.dump_dps():
        if netdev in dpctl.show(dp):
            return 'Error: netdev already exists for datapath or netdev does not exist'
        else:
            dpctl.add_if(dp, netdev)
            return 'Success'
    else:
        return 'Datapath Does Not Exist'

@ovsclient.route('/ovs/delif/<dp>/<netdev>', methods=['GET', 'DELETE'])
def del_if(dp, netdev):
    if dp in dpctl.dump_dps():
        if netdev in dpctl.show(dp):
            dpctl.del_if(dp, netdev)
            return 'Success'
        else:
            return 'netdev is not associated with the datapath'
    else:
        return 'Datapath Does Not Exist'

       

@ovsclient.route('/ovs/showflow/<dp>', methods=['GET'])      
def show_flow(dp):
    if dp in dpctl.dump_dps():
	if dpctl.dump_flows(dp) == None:
	    return dpctl.dump_flows(dp)
        else:
            return 'No Flows'
        
    else:
      return 'Datapath Does Not Exist'
 

@ovsclient.route('/ovs/deleteflow/<dp>', methods=['GET', 'DELETE'])
def delete_flow(dp):
    if dp in dpctl.dump_dps():
        dpctl.del_flows(dp)
        return 'Flows Deleted'
    else:
      return 'Datapath Does Not Exist'
@ovsclient.route('/ovs/showalldp', methods=['GET'])
def show_alldp():
    return dpctl.dump_dps()

@ovsclient.route('/ovs/updateif/<dp>/<port>', methods=['GET'])
def update_if(dp, port):
    if dp in dpctl.dump_dps():
        if port in dpctl.show(dp):
            dpctl.set_if(dp, port)
            return 'Success'
        else:
            return 'netdev is not associated with the datapath'
    else:
        return 'Datapath Does Not Exist'



if __name__ == '__main__':
    ovsclient.run(debug=True)



