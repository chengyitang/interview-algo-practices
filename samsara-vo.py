def markdown_to_html(text):

    """Convert markdown to html; features: paragraphs, linebreak, blockquote, strikethrough"""

    # output list
    output = []

    # split by paragraphs
    paragraphs = text.split('\n\n')

    for para in paragraphs:

        para_html = '<p>'   # html string for this paragraph
        in_block = False     # flag for blockquote scope 

        # split by lines
        lines = para.split('\n')
        for i, line in enumerate(lines):

            #line = line.strip()
            
            # process strikethrough (assume paired)
            while '~~' in line:
                line = line.replace('~~', '<del>', 1)   # opening: replace once
                line = line.replace('~~', '</del>', 1)  # closing: replace once

            # process blockquote
            if line.startswith('>'):
                if not in_block: # opening
                    para_html += '<blockquote>'
                    in_block = True
                para_html += line[1:].strip()
                # not last line -> add linebreak
                if i < len(lines) - 1:
                    para_html += '<br />'
            else:
                if in_block: # closing
                    para_html += '</blockquote>'
                    in_block = False
                para_html += line
                # not last line -> add linebreak
                if i < len(lines) - 1:
                    para_html += '<br />'

        # blockquote not closed in the end of paragraph
        if in_block: 
            para_html += '</blockquote>'
        # close paragraph
        para_html += '</p>'

        output.append(para_html)

    return ''.join(output)    

def main():

    input_str = ("This is a paragraph with a soft\n" + 
             "line break.\n\n" + 
             "This is another paragraph that has\n" + 
             "> Some text that\n" + 
             "> is in a\n" + 
             "> block quote.\n\n" + 
             "This is another paragraph with a ~~strikethrough~~ word.")
    
    expected_html = (
        "<p>This is a paragraph with a soft<br />line break.</p>" +
        "<p>This is another paragraph that has<br /><blockquote> Some text that<br /> is in a<br /> block quote.</blockquote></p>" +
        "<p>This is another paragraph with a <del>strikethrough</del> word.</p>"
    )
    
    result = markdown_to_html(input_str)
    print(result)
    assert result == expected_html, "Wrong result"

if __name__ == "__main__":
    main()