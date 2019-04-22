register() {
	// Initialize Firebase
	var config = {
		apiKey: "AIzaSyAYAf35t-8bGqp-6WsRtSM-sqJqp5z9P_w",
		authDomain: "showme-22fa9.firebaseapp.com",
	    databaseURL: "https://showme-22fa9.firebaseio.com",
		projectId: "showme-22fa9",
		storageBucket: "showme-22fa9.appspot.com",
		messagingSenderId: "336455638979"
	};
	firebase.initializeApp(config);
	var firestore = firebase.firestore();
	
	const docRef = firestore.collection("users").doc(userTextField.value);
	const userTextField = document.querySelector("#reguname");
	const passTextField = document.querySelector("#regpsw");
	const registerBut = document.querySelector("#regButton");
	
	registerBut.addEventListener("click", function() {
		const userSave = userTextField.value;
		const passSave = passTextField.value;
		docRef.set({
			password: passSave
			username: userSave
		}).then(function() {
			console.log("Username and Password saved!");
		}).catch(function (error) {
			console.log("Error received: ", error);
		});
	})
	
}
  