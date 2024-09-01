from main import main

def test_main(mocker):
    mock_bill = mocker.patch("main.Bill")
    mock_flatmate = mocker.patch("main.Flatmate")
    
    mock_pdf_report = mocker.patch("main.PdfReport", autospec=True)
    mock_instance = mock_pdf_report.return_value

    mock_bill_instance = mock_bill.return_value
    mock_flatmate1 = mock_flatmate.return_value
    mock_flatmate2 = mock_flatmate.return_value
    
    mock_flatmate1.name = "John"
    mock_flatmate1.days_in_house = 20
    mock_flatmate2.name = "Marry"
    mock_flatmate2.days_in_house = 25
    mock_bill_instance.amount = 120
    mock_bill_instance.period = "March 2021"
    
    main()
    
    mock_instance.generate.assert_called_once_with(flatmate1=mock_flatmate1, flatmate2=mock_flatmate2, bill=mock_bill_instance)
