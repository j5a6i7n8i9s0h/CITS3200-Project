from docx import Document 


document = Document('test.docx')

document.tables[1].cell(0,0).text = "VAYS"
''' 
 0 table 1: contact details 
 1 table 2: SPECIES / PHENOTYPE / MODEL ISSUES
 2 table 3: MONITORING CRITERIA AND SCORING 
 3 table 4: MONITORING FREQUENCY
 4 table 5: Montiroing Freq : Anathesia , general etc
 5 table 6:	5) ACTIONS AND INTERVENTIONS
 6 table 7: 6)	AEC INTERVENTIONS for Body Weight Loss and Subcutaneous Tumour Size     (as appropriate to the project) 
 7 table 8: 7)	INSTRUCTIONS for the conduct of the monitoring and recording

'''
#print (type(document.tables[0].rows.height))
# for count,val in enumerate(document.tables[0].rows):
#     print count,val
dictionary ={
    'Protocol Title :' : 'corndog',
    'Monitoring Start Date :' : 'today' , 
    'Chief Investigator :' : 'kanye_west' , 
    'Emergency Contact :' : ['asd', ' 123123141342'],
    'Monitor 1 :' : ['sdfsdf', ' 123123141342'],
    'Monitor 2 :' : ['dddddd', ' 123123141342'],
    'Monitor 3 :' : ['ee ', ' 12342'],
    'Person responsible for euthanasia :' : ['hahaha', ' 12'],
    'Other experts :' : ['he', ' 2'],
    
}
for rows in document.tables[0].rows:
        head = rows.cells[0].text
        if head in dictionary:
            if head in ['Protocol Title :', 'Monitoring Start Date :', 'Chief Investigator :']:
                rows.cells[1].paragraphs[0].add_run(dictionary[head]).bold = True
            else: 
                rows.cells[2].paragraphs[0].add_run(dictionary[head][1]).bold = True
                rows.cells[1].paragraphs[0].add_run(dictionary[head][0]).bold = True
document.save('tes2t.docx')