def numUniqueEmails( emails):
    rtn_list = []

    for each_email in emails:
        if '.' in each_email.split('@')[0]:
            each_email = each_email.split('@')[0].replace('.','')+ '@'+each_email.split('@')[1]
        if '+' in each_email:
            each_email = each_email[0:each_email.index('+')]+ each_email[each_email.index('@'):]
        if each_email not in rtn_list:
            rtn_list.append(each_email)

    return len(rtn_list)










if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(numUniqueEmails(emails))