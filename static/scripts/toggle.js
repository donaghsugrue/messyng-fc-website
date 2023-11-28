function toggle(){
    var body = document.body; 
    body.id = ( body.id ) ? body.id : "body_id"; // ffox
    body.use_custom_cursor = !body.use_custom_cursor;
    body.style.cursor = body.use_custom_cursor ? "url(../media/cursor/pink_finger_point.jpg)" : 'auto';

}