// user name validation
const firstName = document.getElementById("firstName");
const firstNameError = document.getElementById("firstNameError");
const lastName = document.getElementById("lastName");
const lastNameError = document.getElementById("lastNameError");
const username = document.getElementById("userName");
const usernameError = document.getElementById("userNameError");
const password = document.getElementById("password");
const passwordError = document.getElementById("passwordError");
const confirmPassword = document.getElementById("confirmPassword");
const confirmPasswordError = document.getElementById("confirmPasswordError");
const email = document.getElementById("email");
const emailError = document.getElementById("emailError");
const terms = document.getElementById("terms");
const submitBtn = document.getElementById("submitBtn");

const buttonClasses = [
  "bg-slate-400",
  "hover:bg-slate-400",
  "hover:text-white",
  "hover:border",
  "hover:border-gray-300",
];



// username validation
username.addEventListener("blur", () => {
  if (username.value === "") {
    usernameError.innerHTML = "Username is required!";
    submitBtn.classList.add(...buttonClasses);
    submitBtn.disabled = true;
  } else {
    usernameError.innerHTML = "";

    submitBtn.disabled = false;
  }
});

// password validation
password.addEventListener("blur", () => {
  if (password.value === "") {
    passwordError.innerHTML = "Password is required";
    submitBtn.classList.add(...buttonClasses);
    submitBtn.disabled = true;
  } else {
    passwordError.innerHTML = "";

    submitBtn.disabled = false;
  }
});

// first name validation
firstName.addEventListener("blur", () => {
  if (firstName.value === "") {
    firstNameError.innerHTML = "First Name is required";
    submitBtn.classList.add(...buttonClasses);
    submitBtn.disabled = true;
  } else {
    firstNameError.innerHTML = "";

    submitBtn.disabled = false;
  }
});

// required field validation
lastName.addEventListener("blur", () => {
  if (lastName.value === "") {
    lastNameError.innerHTML = "Last Name is required";
    submitBtn.classList.add(...buttonClasses);
    submitBtn.disabled = true;
  } else {
    lastNameError.innerHTML = "";

    submitBtn.disabled = false;
  }
});

// required field validation
const passwordValidation = (value) => {
  if (value === "") {
    passwordError.innerHTML = "Password is required";
    submitBtn.classList.add(...buttonClasses);
    submitBtn.disabled = true;
  } else if (value.length < 8) {
    passwordError.innerHTML = "Password must be at least 8 characters long";
    submitBtn.classList.add(...buttonClasses);
    submitBtn.disabled = true;
  } else {
    passwordError.innerHTML = "";

    submitBtn.disabled = false;
  }
};

terms.addEventListener("change", () => {
  if (terms.checked) {
    if (
      password.value === confirmPassword.value &&
      password.value.length >= 8 &&
      email.value !== "" &&
      username.value !== "" &&
      firstName.value !== "" &&
      lastName.value !== ""
    ) {
      submitBtn.classList.remove(...buttonClasses);
      submitBtn.disabled = false;
    } else {
      submitBtn.classList.add(...buttonClasses);
      submitBtn.disabled = true;
    }
  } else {
    submitBtn.classList.add(...buttonClasses);
    submitBtn.disabled = true;
  }
});

// required field validation
const comparePassword = (password, confirmPassword) => {
  if (password !== confirmPassword) {
    confirmPasswordError.innerHTML = "Passwords do not match";
    submitBtn.classList.add(...buttonClasses);
    submitBtn.disabled = true;
  } else {
    confirmPasswordError.innerHTML = "";
    submitBtn.disabled = false;
  }
};

// required field validation
const emailValidation = (email) => {
  if (email === "") {
    emailError.innerHTML = "Email is required";
    submitBtn.classList.add(...buttonClasses);
    submitBtn.disabled = true;
  } else {
    emailError.innerHTML = "";

    submitBtn.disabled = false;
  }
};

// required field validation
password.addEventListener("keydown", () => {
  passwordValidation(password.value);
});

password.addEventListener("keyup", () => {
  passwordValidation(password.value);
});

// required field validation
confirmPassword.addEventListener("keydown", () => {
  comparePassword(password.value, confirmPassword.value);
});
confirmPassword.addEventListener("keyup", () => {
  comparePassword(password.value, confirmPassword.value);
});

// required field validation
email.addEventListener("blur", () => {
  emailValidation(email.value);
});
