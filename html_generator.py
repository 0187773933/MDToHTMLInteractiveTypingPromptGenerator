

def generate( options ):
	return f'''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>{options["title"]}</title>
	<!-- https://www.srihash.org/ -->
	<link rel="stylesheet" href="https://39363.org/CDN/jquery-ui.css" integrity="sha256-RPilbUJ5F7X6DdeTO6VFZ5vl5rO5MJnmSk4pwhWfV8A=" >
	<script src="https://39363.org/CDN/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="></script>
	<link rel="stylesheet" href="https://39363.org/CDN/bootstrap.min.css" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We">
	<script src="https://39363.org/CDN/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj"></script>
	<script src="https://39363.org/CDN/jquery-ui.min.js" integrity="sha256-VazP97ZCwtekAsvgPBSUwPFKdrwD3unUfSGVYrahUqU=" ></script>
	<link rel="stylesheet" href="https://39363.org/CDN/katex/katex.min.css" integrity="sha256-M6KFoDq9eUpmogkDgw6+3R3ZgUPSuFXnQyr8tskSfQs=">
	<script src="https://39363.org/CDN/katex/katex.min.js" integrity="sha256-FyuFDgL3AT2Wi7dlv82fSVvxe2rPx1rRSVtMOWeRp6k="></script>
	<script src="https://39363.org/CDN/katex/mhchem.min.js" integrity="sha256-rdVHJ96CTjgtCSJGnAZzhrvBOklMB9jN1B6oyg5J8uU="></script>
	<script src="https://39363.org/CDN/katex/auto-render.min.js" integrity="sha256-G53bYZLObbTLTA3j70xRGPKxKYlBbzvDZ789B6sSFkE="></script>
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
	<div class="container">
		<!-- <div class="row justify-content-center" style="border: 1px solid red"> -->
		<div class="row justify-content-center">
			<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 our-no-gutter">
				<div class="card" style="background-color: #363B40;">
					<div class="card-header text-center">
						<div id="card-title-content"></div>
					</div>
					<div class="card-body slimmed-padding" id="card-body-container">
						<div id="card-body-content"></div>
					</div>
				</div>
			</div>
		</div>
		<br></br>
		<!-- <div class="row justify-content-center fixed-row-bottom" id="row-navigation" style="border: 1px solid green"> -->
		<div class="row justify-content-center fixed-row-bottom" id="row-navigation">
			<div class="col text-center">
				<div>
					<span id="current-card-number"></span>&nbsp;&nbsp;&nbsp;
					<span id="previous-button" class="previous-button">&#8249;</span>&nbsp;&nbsp;&nbsp;
					<span id="next-button" class="next-button">&#8250;</span>&nbsp;&nbsp;&nbsp;
					<span id="total-cards"></span>
				</div>
			</div>
		</div>
		<!-- <div class="row justify-content-center" id="row-grading" style="border: 1px solid blue"> -->
		<div class="row justify-content-center" id="row-grading">
			<div class="col text-center">
				<!-- https://getbootstrap.com/docs/5.0/customize/color/ -->
				<button type="button" class="btn btn-danger">Again</button>&nbsp;
				<button type="button" class="btn btn-warning">Hard</button>&nbsp;
				<button type="button" class="btn btn-success">Good</button>&nbsp;
				<button type="button" class="btn btn-primary">Easy</button>
			</div>
		</div>
		<div class="row justify-content-center">
			<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 our-no-gutter">
				<!-- https://getbootstrap.com/docs/5.0/utilities/sizing/ -->
				<!-- <div id="row-extra-space" style="height: 80vh; border: 1px solid yellow"></div> -->
				<div id="row-extra-space" style="height: 80vh;"></div>
			</div>
		</div>
	</div>

	<script type="text/javascript">

		function previous_prompt() {{

		}}
		function next_prompt() {{

		}}
		function render_katex() {{
			renderMathInElement( document.body , {{
				strict: "ignore" ,
				delimiters: [ // https://stackoverflow.com/a/45301641
					{{ left: "$$" , right: "$$" , display: true }} ,
					{{ left: "\\[" , right: "\\]" , display: true }} ,
					{{ left: "$" , right: "$" , display: false }} ,
					{{ left: "\\(" , right: "\\)" , display: false }}
				]
			}});
		}}
		//$( "#card-title-content" ).html( `<h3>${{window.DECK.questions[ window.DECK.active_index ].prompt}}</h3>` );

		function init() {{
			render_katex();
		}}
		document.addEventListener( "DOMContentLoaded" , init );
	</script>
</body>
</html>
'''