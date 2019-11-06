def removeComments( source):
    rtn_list = []
    open_flag = False
    for each_line in source:
        if open_flag:
            if len(each_line.split('*/')) > 1:
                if each_line.split('*/')[1]:
                    if len(rtn_list) == 0:
                        rtn_list.append(each_line.split('*/')[1])
                    else:
                        last_eme = rtn_list[len(rtn_list) - 1] + each_line.split('*/')[1]
                        rtn_list[len(rtn_list) - 1] = last_eme

                open_flag = False
        else:
            if '//' in each_line and '/*' in each_line:
                if each_line.index('//') < each_line.index('/*'):
                    if len(each_line.split('//')) > 1:
                        if each_line.split('//')[0]:
                            rtn_list.append(each_line.split('//')[0])

                else:
                    if len(each_line.split('/*')) > 1:
                        if each_line.split('/*')[0]:
                            rtn_list.append(each_line.split('/*')[0])
                        open_flag = True
                        if len(each_line.split('*/')) > 1:
                            if each_line.split('*/')[len(each_line.split('*/')) - 1]:
                                if len(rtn_list) == 0:
                                    rtn_list.append(each_line.split('*/')[len(each_line.split('*/')) - 1])
                                else:
                                    last_eme = rtn_list[len(rtn_list) - 1] + each_line.split('*/')[
                                        len(each_line.split('*/')) - 1]
                                    rtn_list[len(rtn_list) - 1] = last_eme

                            open_flag = False

            else:
                if len(each_line.split('/*')) > 1:
                    if each_line.split('/*')[0]:
                        rtn_list.append(each_line.split('/*')[0])
                    open_flag = True
                    if len(each_line.split('*/')) > 1:
                        if each_line.split('*/')[len(each_line.split('*/')) - 1]:
                            if len(rtn_list) == 0:
                                rtn_list.append(each_line.split('*/')[len(each_line.split('*/')) - 1])
                            else:
                                last_eme = rtn_list[len(rtn_list) - 1] + each_line.split('*/')[
                                    len(each_line.split('*/')) - 1]
                                rtn_list[len(rtn_list) - 1] = last_eme

                        open_flag = False

                elif len(each_line.split('//')) > 1:
                    if each_line.split('//')[0]:
                        rtn_list.append(each_line.split('//')[0])
                    continue
                else:
                    rtn_list.append(each_line)
    return (rtn_list)










if __name__ == '__main__':
    source =["void func(int k) {", "/* this function does nothing */ nithin // veer ", "   k = k*2/4;", "   k = k/2;*/", "}"]
    print(removeComments(source))