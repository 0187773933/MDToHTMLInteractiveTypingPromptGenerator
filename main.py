#!/usr/bin/env python3
import sys
import re
from pathlib import Path
import markdown

import html_generator

def write_text( file_path , text_lines_list ):
	#with open( file_path , 'a', encoding='utf-8' ) as f:
	with open( file_path , 'w', encoding='utf-8' ) as f:
		f.writelines( text_lines_list )

def read_text( file_path ):
	with open( file_path ) as f:
		return f.read().splitlines()

def replace_interactive_spans_with_input_fields( input_md_lines ):
	output_lines = []
	span_matching_text = '<span class="interactive-typing-prompt"'
	for index , line in enumerate( input_md_lines ):

		if span_matching_text in line:
			print( f"{index} === {line}" )
			starts = [ [ match.start() , match.end() ] for match in re.finditer( span_matching_text , line ) ]
			stops = [ line.find( "</span>" , x[ 1 ] ) for x in starts ]
			rebuilt_line = ""
			intermediate_index = 0
			for match_index , match in enumerate( starts ):
				# 1.) append everything up until 'this' match
				rebuilt_line += line[ intermediate_index : match[ 0 ] ]

				# 2.) build input html for 'this' match
				end_of_span_opening_index = ( line.find( '">' , match[ 1 ] ) + 2 )
				existing_text = line[ end_of_span_opening_index : stops[ match_index ] ]
				# built_input_html = f'<input type="text" class="interactive-typing-prompt-input" size="3" name="{existing_text}">'
				built_input_html = f'<span><input type="text" class="interactive-typing-prompt-input" style="width: {len(existing_text)+1}ch;" name="{existing_text}"> <span class="hint">&#63;</span></span>'
				rebuilt_line += built_input_html
				# 3.) update intermediate index for next round
				intermediate_index = stops[ match_index ]

			# get any final text after the last match
			rebuilt_line += line[ intermediate_index : ]
			output_lines.append( rebuilt_line )
		else:
			output_lines.append( line )
	return output_lines

if __name__ == "__main__":

	# 0.) Prep
	input_md_fp = Path( sys.argv[ 1 ] )
	output_html_fp = input_md_fp.parent.joinpath( f"{input_md_fp.stem}.html" )
	input_md = read_text( str( input_md_fp ) )

	# 1.) Conversion
	input_md = replace_interactive_spans_with_input_fields( input_md )
	input_html = markdown.markdown( "\n".join( input_md ) )
	print( input_html )

	# 2.) Generate Interactive HTML File
	# html = html_generator.generate({
	# 	"title": "Test Interactive MD"
	# })
	# write_text( str( output_html_fp ) , html )




