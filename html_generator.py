

def generate( options ):
	return f'''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>{options["title"]}</title>
	<!-- https://www.srihash.org/ -->
	<link rel="stylesheet" href="https://39363.org/CDN/jquery-ui.css">
	<script src="https://39363.org/CDN/jquery-3.6.0.min.js"></script>
	<link rel="stylesheet" href="https://39363.org/CDN/bootstrap.min.css">
	<script src="https://39363.org/CDN/bootstrap.bundle.min.js"></script>
	<script src="https://39363.org/CDN/jquery-ui.min.js"></script>
	<link rel="stylesheet" href="https://39363.org/CDN/katex/katex.min.css">
	<script src="https://39363.org/CDN/katex/katex.min.js"></script>
	<script src="https://39363.org/CDN/katex/mhchem.min.js"></script>
	<script src="https://39363.org/CDN/katex/auto-render.min.js"></script>
	<style type="text/css">
	 	body {{
			background-color: #2E3033;
			color: #b8bfc6;
		}}
		.next-button {{
			text-decoration: none;
			display: inline-block;
			padding: 8px 16px;
			border-radius: 50%;
			background-color: #b7b7b7;
			color: white;
		}}
		.previous-button {{
			text-decoration: none;
			display: inline-block;
			padding: 8px 16px;
			border-radius: 50%;
			background-color: #b7b7b7;
			color: white;
		}}
		.our-no-gutter {{
			margin-left: 0;
			margin-right: 0;
			padding-left: 0;
			padding-right: 0;
		}}
		.slimmed-padding {{
			margin-left: 0 !important;
			margin-right: 0 !important;
			padding-left: 1 !important;
			padding-right: 1 !important;
		}}
		.correct {{
			border: 2px solid green;
		}}
	</style>
</head>
<body>
	<br>
	<div class="container">
		<div class="row slimmed-padding">
			{options["input"]}
		</div>
	</div>

	<script type="text/javascript">
		function validate_typing_prompt_input( event ) {{
			if ( event.key === "Control" ) {{
				// console.log( "pressed the control key" );
				$( event.currentTarget ).parent().replaceWith( `<span style="border: 2px solid green">${{event.currentTarget.name}}</span>` );
				return;
			}}
			if ( $( event.currentTarget ).val().trim() === event.currentTarget.name ) {{
				console.log( "correct" );
				$( event.currentTarget ).parent().replaceWith( `<span style="border: 2px solid green">${{event.currentTarget.name}}</span>` );
			}}
		}}
		function render_katex() {{
			renderMathInElement( document.body , {{
				strict: "ignore" ,
				delimiters: [ // https://stackoverflow.com/a/45301641
					{{ left: "$$" , right: "$$" , display: true }} ,
					// {{ left: "\\[" , right: "\\]" , display: true }} ,
					{{ left: "$" , right: "$" , display: false }} ,
					// {{ left: "\\(" , right: "\\)" , display: false }}
				]
			}});
		}}
		function setup_hooks() {{
			$( document ).on( "keyup" , ".interactive-typing-prompt-input" , ( event ) => {{
				validate_typing_prompt_input( event );
			}});
			$( document ).on( "click" , ".hint" , ( event ) => {{
				let target_name = $( event.currentTarget ).prev().attr( "name" );
				$( event.currentTarget ).prev().val( target_name );
				setTimeout( function() {{
					$( event.currentTarget ).prev().val( "" );
				}} , 1500 );
			}});
		}}
		function init() {{
			$( document ).ready( function(){{
				$( ".interactive-typing-prompt-input" ).each( ( index , element ) => {{
					$( element ).val( "" );
				}});
				render_katex();
				setup_hooks();
			}});
		}}
		document.addEventListener( "DOMContentLoaded" , init );
	</script>
</body>
</html>
'''