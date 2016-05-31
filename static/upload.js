// source code (GPLv2) : http://www.plupload.com/examples/core  (hier für privaten Zweck modifiziert)

$(function() {
	document.getElementById('console').innerHTML += "WARNING: Uploading files with Spaces, Braces etc. \n         in the filename doesn't work!";
	var uploader = new plupload.Uploader({
		runtimes : 'html5,flash,silverlight,html4',
		browse_button : 'browse', // you can pass in id...
		container: document.getElementById('controls'), // ... or DOM Element itself
		
		// url of a server-side handler, that will accept the files, do some security checks on them and finally move them to a destination folder. 
		url : "/up", // Python-Main-Script will handle this POST-Request.
		
		filters : {
			max_file_size : '10mb',
			mime_types: [
				{title : "Image files", extensions : "jpg,gif,png"}//,
				//{title : "Zip files", extensions : "zip"}
			]
		},
		
		// Downsize auf CLIENT-Seite --> Performanz!
		resize: {
			width: 40,
			height: 40
		},
		
		// Flash settings
		flash_swf_url : '../static/plupload218/js/Moxie.swf',
		
		// Silverlight settings
		silverlight_xap_url : '../static/plupload218/js/Moxie.xap',
		
		init: {
			PostInit: function() {
				document.getElementById('filelist').innerHTML = '';
				var clickedBrowse = false;
				
				document.getElementById('browse').onclick = function() {
					document.getElementById('start-upload').className = "btn-primary";
					clickedBrowse = true;
					return false;
				};
				
				document.getElementById('start-upload').onclick = function() {
					if (clickedBrowse) {
						document.getElementById('browse').className = "btn-default";
						document.getElementById('start-upload').className = "btn-default";
						document.getElementById('controls').innerHTML += '\n<button id="moveImg" onclick="moveMyPictures()" class="btn-success">Feel the magic</button>';
						uploader.start();
					}
					return false;
				};
			},
	 
			FilesAdded: function(up, files) {
				document.getElementById('filelist-headline').innerHTML = "<h3>Your files</h3>";
				document.getElementById('filelist').classList.add('dash-me');
				plupload.each(files, function(file) {
					document.getElementById('filelist').innerHTML += '<div id="' + file.id + '">' + file.name + ' (' + plupload.formatSize(file.size) + ') <b></b></div>';
				});
			},
	 
			UploadProgress: function(up, file) {
				document.getElementById(file.id).getElementsByTagName('b')[0].innerHTML = '<span>' + file.percent + "%</span>";
				var pics = document.getElementById('pictureShow');
				//debugger;
				if (file.percent == 100 ) {
					// file.name als Bedingung allein reicht nicht, weil "testbild.png" in "palette-testbild.png" vorkommt, und "testbild.png" als zweites Bild dann nicht mehr angezeigt wuerde.
					if (pics.innerHTML.contains('uploads/'+file.name)) {
						// task finished. no more need to do anything here.
					}
					else {
						pics.innerHTML += '<img height="40" width="40" alt="uploadedPic" src="../static/uploads/'+file.name+'"><br />';
					}
				}
			},

			Error: function(up, err) {
				document.getElementById('console').innerHTML += "Error #" + err.code + ": " + err.message + "\n";
			}
		}
		
	});
	uploader.init();
});