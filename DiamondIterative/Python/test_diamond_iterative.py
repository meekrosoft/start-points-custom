import diamond

 
def test_DiamondA_has_one_line_containing_A():
	assert diamond.Diamond('A').print_diamond() == "A"

def ignore_DiamondB_prints_a_char_sequence_for_the_top_half():
	assert diamond.Diamond('B').print_diamond() == "AB"

def ignore_DiamondB_prints_a_char_sequence_for_the_top_and_bottom__halves():
	assert diamond.Diamond('B').print_diamond() == "ABA"

def ignore_DiamondC_prints_a_char_sequence_for_the_top_and_bottom__halves():
	assert diamond.Diamond('C').print_diamond() == "ABCBA"

def ignore_DiamondB_separates_rows():
	assert diamond.Diamond('B').print_diamond() == "A\nB\nA"

def ignore_DiamondB_indents_first_and_last_rows():
	assert diamond.Diamond('B').print_diamond() == " A\nB\n A"

def ignore_DiamondC_indents_all_rows_except_middle():
	assert diamond.Diamond('C').print_diamond() == """\
  A
 B
C
 B
  A"""

def ignore_DiamondB_duplicates_the_middle_B():
	assert diamond.Diamond('B').print_diamond() == " A\nBB\n A"

def ignore_DiamondC_duplicates_letters_on_middle_rows():
	assert diamond.Diamond('C').print_diamond() == """\
  A
 BB
CC
 BB
  A"""

def ignore_DiamondB_has_a_space_between_the_two_Bs():
	assert diamond.Diamond('B').print_diamond() == " A\nB B\n A"
 
def ignore_DiamondC_has_spaces_on_middle_rows():
	assert diamond.Diamond('C').print_diamond() == """\
  A
 B B
C   C
 B B
  A"""

def ignore_DiamondD_is_correct():
	assert diamond.Diamond('D').print_diamond() == """\
   A
  B B
 C   C
D     D
 C   C
  B B
   A"""
