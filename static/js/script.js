// table dropdown
window.onload = function () {
       const activeTabContent = localStorage.getItem("activeTabContent");
       if(activeTabContent){
            openCity(null, activeTabContent);
       }
}

function openCity(evt, cityName) {
  if (cityName) {
      var i, tabcontent, tablinks;
      tabcontent = document.getElementsByClassName("tabcontent");
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
      }
      tablinks = document.getElementsByClassName("tablinks");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
      }
      document.getElementById(cityName).style.display = "block";
      if (evt) {
          evt.currentTarget.className += " active";
          }

      localStorage.setItem('activeTabContent', cityName);
    }
}

// clearLocalStorage.js

function clearLocalStorage() {
  localStorage.removeItem('activeTabContent');
}


// connfirm update document

function confirmDelete(documentId) {
  if (confirm('Are you sure you want to delete this object?')) {
    // Submit the delete form if the user confirms the delete
    document.getElementById('delete-form-'+documentId).submit();
  }
}

function confirmUpdate(documentId) {
  if (confirm('Are you sure you want to update distribution?')) {
    document.getElementById('update-distribution-'+documentId).submit();
  }
}

// progress bar
const pdf = document.getElementById('id_pdf_file');
if(pdf) {
 pdf.addEventListener('change', progressBar());
 }
// get the input event listener ( ERROR INPUT MSH NOT DEFINED GRGR DIDALEM FORM)

    function progressBar(){
        const uploadForm = document.getElementById('upload-form');
        const alertBox = document.getElementById('alert-box');
        const progressBox = document.getElementById('progress-box');
        const cancelBox = document.getElementById('cancel-box');
        const cancelBtn = document.getElementById('cancel-button');
        const csrfInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
        const csrfValue = csrfInput.value;
         // add event listener when id_pdf_file is changed
        pdf.addEventListener('change', ()=>{
            progressBox.classList.remove('not-visible');
            cancelBox.classList.remove('not-visible');
            const pdfData = pdf.files[0];
            const fd = new FormData()
            fd.append('csrfmiddlewaretoken', csrfValue)
            fd.append('pdf_file', pdfData)

            $.ajax({
                type :'POST',
                url : uploadForm.action,
                enctype : 'multipart/form-data',
                data : fd,
                beforeSend : function(){
                    alertBox.innerHTML = "" // reset the alertbox kalo upload ulang


                },
                xhr : function(){
                    const xhr = new window.XMLHttpRequest();
                    xhr.upload.addEventListener('progress', e=>{
                        const percent = e.loaded / e.total * 100
                        console.log(e)
                        console.log(percent)
                        if(e.lengthComputable){
                               progressBox.innerHTML = '<div class="progress"> <div class="progress-bar" role="progressbar" style="width: '+ percent + '%" aria-valuenow="'+ percent + '" aria-valuemin="0" aria-valuemax="100"></div> </div> <p> '+ percent.toFixed(1) +' % Completed </p>'
                    }
                    });

                    cancelBtn.addEventListener('click', ()=>{
                        xhr.abort();
                        setTimeout( ()=> {
                            uploadForm.reset();
                            progressBox.innerHTML ="" ;
                            cancelBox.classList.add('not-visible');
                            alertBox.classList.add('not-visible');
                        }, 200 )
                    })
                    return xhr;
                },

                success : function(response){
                     alertBox.innerHTML = '<div class="alert alert-success" role="alert"> PDF Fully Uploaded  </div>'  ;
                     cancelBox.classList.add('not-visible');

                },
                error : function(error){
                      alertBox.innerHTML = '<div class="alert alert-danger" role="alert"> Oops Something when Wrong </div>'
                },
                cache : false,
                contentType: false,
                processData : false,

            })


         });


    }



// PASSWORD HELPER (blom dilanjutkan)

var myInput = document.getElementById("id_password1");
// When the user clicks on the password field, show the message box

function showPasswordValidator() {
    document.getElementById("password-confirmation-message").style.display = "block";
}

function hidePasswordValidator() {
    document.getElementById("password-confirmation-message").style.display = "none";
}

// When the user starts to type something inside the password field

async function validatePassword1() {
      var similar = document.getElementById("similar-password");
    var character = document.getElementById("character-password");
    var common = document.getElementById("common-password");
    var number = document.getElementById("number-password");
      const csrfInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
      const csrfValue = csrfInput.value;
      const password = myInput.value;
      // Make a request to the Django backend to check the password against the validators
      const response = await fetch( /password_validation/, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfValue  // set the CSRF token here
        },
        body: JSON.stringify({password})
      });
      const result = await response.json();


      // Validate length
      if (result.length) {
        character.classList.remove("invalid");
        character.classList.add("valid");
      } else {
        character.classList.remove("valid");
        character.classList.add("invalid");
      }

      // Validate cant be commonly used password
      if (result.common) {
        common.classList.remove("invalid");
        common.classList.add("valid");
      } else {
        common.classList.remove("valid");
        common.classList.add("invalid");
      }

      // Validate cant be entirely numeric
      if (result.numeric) {
        number.classList.remove("invalid");
        number.classList.add("valid");
      } else {
        number.classList.remove("valid");
        number.classList.add("invalid");
      }
}

function showPasswordValidator2() {
    document.getElementById("password-confirmation-message2").style.display = "block";
}

function hidePasswordValidator2() {
    document.getElementById("password-confirmation-message2").style.display = "none";
}


function validatePassword2(){
    var myInput2 = document.getElementById("id_password2");
    var same = document.getElementById('same-password')
    password1 = myInput.value;
    password2 = myInput2.value;
    if (password1 == password2) {
        same.classList.remove("invalid");
        same.classList.add("valid");
      } else {
        same.classList.remove("valid");
        same.classList.add("invalid");
      }
}



