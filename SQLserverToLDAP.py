#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymssql  
import ldap
import ldap.modlist



conn = pymssql.connect(host='192.168.x.x', user='sa', password='xx', database='xx', charset="utf8") 
cursor = conn.cursor()  
# For Example, Type Your SQL Statement
cursor.execute("SELECT  hr.id,hr.loginid,hr.password,hr.lastname,hr.mobile AS mobile,hr.managerid AS managerid,hr.subcompanyid1 AS companyId,cf.field3 AS adminUserRank,hr.email,hr.workcode,CONVERT (datetime,hr.lastlogindate,101) AS updateAt,hr.departmentid,hd.departmentname FROM HrmResource hr LEFT JOIN HrmDepartment hd ON hr.departmentid = hd.id LEFT JOIN cus_fielddata cf ON hr.id = cf.id AND cf.scopeid = - 1 WHERE hr.loginid != '' AND hr.password != '';")

#print cursor.fetchall()

def searchUser(user):
    try:
        l = ldap.open('ldap.xx.com')
        l.protocol_version = ldap.VERSION3
        username = "cn=admin,dc=xx,dc=com"
        password  = "xx"
        l.simple_bind(username, password)

    except ldap.LDAPError, e:
        print e

    baseDN = "dc=xx,dc=com"
    searchScope = ldap.SCOPE_SUBTREE
    retrieveAttributes = None
    searchFilter = "uid=*" + user
    try:
        ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
        result_set = []
        while l:
            result_type, result_data = l.result(ldap_result_id, 0)
            #print result_data
            if (result_data == []):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)
        #print result_set 
        return result_set 
    except ldap.LDAPError, e:
        print e


row = cursor.fetchone()  
while row:  
