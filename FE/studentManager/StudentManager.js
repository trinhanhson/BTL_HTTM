let student = JSON.parse(sessionStorage.getItem("student"));

var table = document.getElementById("table");
var studentCode = table.rows[0].cells;
studentCode[1].innerHTML = student.studentCode;
var nameStudent = table.rows[1].cells;
nameStudent[1].innerHTML = student.nameStudent;
var dateOfBirth = table.rows[2].cells;
dateOfBirth[1].innerHTML = student.dateOfBirth;
var gender = table.rows[3].cells;
gender[1].innerHTML = student.gender;

document.getElementById("ok").style.display = "none";

function change() {
    studentCode[1].innerHTML = "";
    var inputStudentCode = document.createElement('input');
    inputStudentCode.type = "text";
    inputStudentCode.value = student.studentCode;
    studentCode[1].appendChild(inputStudentCode);
    nameStudent[1].innerHTML = "";
    var inputNameStudent = document.createElement('input');
    inputNameStudent.type = "text";
    inputNameStudent.value = student.nameStudent;
    nameStudent[1].appendChild(inputNameStudent);
    dateOfBirth[1].innerHTML = "";
    var inputDateOfBirth = document.createElement('input');
    inputDateOfBirth.type = "text";
    inputDateOfBirth.value = student.dateOfBirth;
    dateOfBirth[1].appendChild(inputDateOfBirth);
    gender[1].innerHTML = "";
    var inputGender = document.createElement('input');
    inputGender.type = "text";
    inputGender.value = student.gender;
    gender[1].appendChild(inputGender);

    document.getElementById("change").style.display = "none";
    document.getElementById("ok").style.display = "inline";
}

function ok() {
    studentCode[1].innerHTML = studentCode[1].childNodes[0].value;
    nameStudent[1].innerHTML = nameStudent[1].childNodes[0].value;
    dateOfBirth[1].innerHTML = dateOfBirth[1].childNodes[0].value;
    gender[1].innerHTML = gender[1].childNodes[0].value;
}