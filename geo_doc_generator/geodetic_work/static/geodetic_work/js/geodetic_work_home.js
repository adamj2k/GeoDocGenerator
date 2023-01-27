function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

async function deleteWork(buttonID){
    let elems = buttonID.split("-");
    let sentID = elems[elems.length - 1]

    let resp = await fetch(`/georestapi/workdeleteapi/${sentID}`,
    { method: 'DELETE',
      headers: {'Content-Type': 'application/json', 'X-CSRFToken': getCookie("csrftoken")},
    });
    let status_code = await resp.status_code;

    console.log(status_code);
    if(status_code == 204) {
        reload();
    }
}

async function editWork(buttonID){
    let elems = buttonID.split("-");
    let sentID = elems[elems.length - 1]

    let resp = await fetch(`/georestapi/workeditapi/${sentID}`,
    {'method': 'PUT',
      headers: {'Content-Type': 'application/json', 'X-CSRFToken': getCookie("csrftoken")},
    });
    let status_code = await resp.status_code;

    console.log(status_code);
    if(status_code == 204) {
        reload();
    }
}
