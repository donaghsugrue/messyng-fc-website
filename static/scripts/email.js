/* js */
function gmail() {
    let carName = "Volvo";
    // code here CAN use carName

    import imaplib
    obj = imaplib.IMAP4_SSL("imap.gmail.com", "993")
    obj.login("messyngband@gmail.com", "m3ssyng18")
    obj.select()

    mail_string_1 = str(obj.search(None, "UnSeen"))
    mail_string_2 = mail_string_1[10:]
    mail_string_3 = mail_string_2[:-2]
    mail_string = int(len(mail_string_3)/2)

    if (mail_string == 0) {
    return "Mail";
    } else {
    return "Mail (" + mail_string + ")"
    }
}





// // python

// def unread_email():
//     import imaplib
//     obj = imaplib.IMAP4_SSL("imap.gmail.com", "993")
//     obj.login("messyngband@gmail.com", "m3ssyng18")
//     obj.select()

//     mail_string_1 = str(obj.search(None, "UnSeen"))
//     mail_string_2 = mail_string_1[10:]
//     mail_string_3 = mail_string_2[:-2]
//     mail_string = int(len(mail_string_3)/2)
//     if mail_string == 0:
//         return "Mail"
//     else:
//         return "Mail (" + mail_string + ")"

// print(unread_email())
