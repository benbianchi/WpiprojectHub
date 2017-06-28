/* particlesJS.load(@dom-id, @path-json, @callback (optional)); */
console.log('callback - particles.js searching for config...');
particlesJS.load('particles-js', 'static/particlesconfig.json', function() {
  console.log('callback - particles.js config loaded');
});