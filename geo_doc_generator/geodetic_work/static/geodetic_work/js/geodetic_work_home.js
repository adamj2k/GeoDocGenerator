async function deleteWork(buttonID){
    let elems = buttonID.split("-");
    let sentID = elems[elems.length - 1]

    let resp = await fetch(`/delete/work/${sentID}`, {'method': 'DELETE'});
    let status_code = await resp.status_code;

    console.log(status_code);
    if(status_code == 204) {
        reload();
    }
}

function editWork(buttonID){

}
