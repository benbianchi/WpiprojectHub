/**
 * @name login
 * @desc Try to log in with email `email` and password `password`
 * @param {string} email The email entered by the user
 * @param {string} password The password entered by the user
 * @returns {Promise}
 * @memberOf thinkster.authentication.services.Authentication
 */
function login(email, password) {
  return $http.post('/api/v1/auth/login/', {
    email: email, password: password
  }).then(loginSuccessFn, loginErrorFn);

  /**
   * @name loginSuccessFn
   * @desc Set the authenticated account and redirect to index
   */
  function loginSuccessFn(data, status, headers, config) {
    Authentication.setAuthenticatedAccount(data.data);

    window.location = '/';
  }

  /**
   * @name loginErrorFn
   * @desc Log "Epic failure!" to the console
   */
  function loginErrorFn(data, status, headers, config) {
    console.error('Epic failure!');
  }
}