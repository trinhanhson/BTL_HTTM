class Student {
    constructor(id, studentCode, nameStudent, dateOfBirth, gender) {
        this.id = id;
        this.studentCode = studentCode;
        this.nameStudent = nameStudent;
        this.dateOfBirth = dateOfBirth;
        this.gender = gender;
    }
}

function loadData() {
    var table = document.getElementById("table");
    const studentList = [];
    for (let i = 0; i < 2; i++) {
        var id = i;
        var studentCode = "B19DCCN562";
        var nameStudent = "Trịnh Anh Sơn";
        var dateOfBirth = "20/12/2001";
        var gender = "Nam";
        let student = new Student(id, studentCode, nameStudent, dateOfBirth, gender);
        studentList.push(student);
        var row = table.insertRow(-1);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        var cell5 = row.insertCell(4);
        cell1.innerHTML = studentCode;
        cell2.innerHTML = nameStudent;
        cell3.innerHTML = dateOfBirth;
        cell4.innerHTML = gender;
        var btnQLVT = document.createElement('input');
        btnQLVT.className = "inputQL";
        btnQLVT.type = "button";
        btnQLVT.value = "QLVT";
        btnQLVT.onclick = function () {
            sessionStorage.setItem("student", JSON.stringify([student.id, student.name]));
            window.location.href = "../fingerprintManager/FingerprintManagager.html"
        }
        var btnQLTT = document.createElement('input');
        btnQLTT.className = "inputQL";
        btnQLTT.type = "button";
        btnQLTT.value = "QLTT";
        btnQLTT.onclick = function () {
            sessionStorage.setItem("student", JSON.stringify(student));
            window.location.href = "../studentManager/StudentManager.html"
        }
        cell5.appendChild(btnQLVT);
        cell5.appendChild(btnQLTT);
    }
}