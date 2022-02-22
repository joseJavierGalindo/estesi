from pyobigram.utils import sizeof_fmt

def createDownloading(filename,totalBits,currentBits,speed,tid=''):
    msg = 'Descargando... \n\n'
    msg+= 'Nombre: ' + str(filename)+'\n'
    msg+= 'Tamaño Total: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= 'Descargado: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= 'Velocidad: ' + str(sizeof_fmt(speed))+'/s\n\n'
    if tid!='':
        msg+= '/cancel_' + tid
    return msg
def createUploading(filename,totalBits,currentBits,speed,originalname=''):
    msg = 'Subiendo A La Nube... \n\n'
    msg+= 'Nombre: ' + str(filename)+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= 'Subiendo: ' + str(filename)+'\n'
    msg+= 'Tamaño Total: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= 'Subido: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= 'Velocidad: ' + str(sizeof_fmt(speed))+'/s\n'
    return msg
def createCompresing(filename,filesize,splitsize):
    msg = 'Comprimiendo... \n\n'
    msg+= 'Nombre: ' + str(filename)+'\n'
    msg+= 'Tamaño Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= 'Tamaño Partes: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= 'Cantidad Partes: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,split_size,current,count,findex):
    msg = 'Proceso Finalizado\n\n'
    msg+= 'Nombre: ' + str(filename)+'\n'
    msg+= 'Tamaño Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= 'Tamaño Partes: ' + str(sizeof_fmt(split_size))+'\n'
    msg+= 'Partes Subidas: ' + str(current) + '/' + str(count) +'\n\n'
    msg+= '🗑Borrar Archivo: ' + '/del_'+str(findex)
    return msg
def createFileMsg(filename,files):
    import urllib
    msg= '<b>🖇Enlaces🖇</b>\n'
    for f in files:
        url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
        #msg+= '<a href="'+f['url']+'">' + f['name'] + '</a>'
        msg+= "<a href='"+url+"'>"+f['name']+'</a>\n'
    return msg
def createFilesMsg(evfiles):
    msg = 'Archivos ('+str(len(evfiles))+')\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = 'Condiguraciones De Usuario\n\n'
    msg+= 'Nombre: @' + str(username)+'\n'
    msg+= 'Moodle User: ' + str(userdata['moodle_user'])+'\n'
    msg+= 'Moodle Password: ' + str(userdata['moodle_password'])+'\n'
    msg+= 'Moodle Host: ' + str(userdata['moodle_host'])+'\n'
    msg+= 'Moodle RepoID: ' + str(userdata['moodle_repo_id'])+'\n'
    msg+= 'Tamaño de Zips : ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = 'No'
    if isadmin:
        msgAdmin = 'Si'
    msg+= 'Admin : ' + msgAdmin + '\n'
    msg+= 'Configurar Moodle\nEjemplo /account user,password'
    return msg
