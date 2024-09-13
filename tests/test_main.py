from pdf_report import PdfReport, FileSharer
from main import main

def test_main(mocker):
    mocker.patch("builtins.input", side_effect=["200", "January 2025", "Luigi", "Yassine", "20", "25"])
    mock_print = mocker.patch("builtins.print")
    mock_generate = mocker.patch.object(PdfReport, "generate")
    mocker.patch.object(FileSharer, "share", return_value="http://someurl.com/sharedfile")
        
    main()
    
    mock_print.assert_any_call("Luigi pays: £88.89")
    mock_print.assert_any_call("Yassine pays: £111.11")
    
    mock_generate.assert_called_once()
    
    mock_print.assert_any_call("http://someurl.com/sharedfile")
