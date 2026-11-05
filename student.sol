// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    struct Student {                     // structure
        uint id;
        string name;
        uint marks;
    }

    Student[] public students;           // dynamic array of structures
    uint public nextId = 0;

    function addStudent(string memory name, uint marks) public {
        students.push(Student(nextId, name, marks));
        nextId++;
    }

    function getStudent(uint index) public view returns (uint, string memory, uint) {
        require(index < students.length, "Invalid index");
        Student memory s = students[index];
        return (s.id, s.name, s.marks);
    }

    function totalStudents() public view returns (uint) {
        return students.length;
    }

    receive() external payable {}        // plain Ether without data
    fallback() external payable {}       // call to a function that does not exist
}
