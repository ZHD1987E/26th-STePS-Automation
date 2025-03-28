function fetchCSVData() {
  var url = "https://raw.githubusercontent.com/ZHD1987E/26th-STePS-Automation/refs/heads/main/26th-steps-awardees.csv"; // Replace with your actual CSV URL
  var response = UrlFetchApp.fetch(url);
  var csvData = response.getContentText(); // Get the CSV as text
  var data = Utilities.parseCsv(csvData); // Convert CSV to a 2D array
  
  Logger.log(data); // View the parsed data
  
  // OPTIONAL: Paste data into a Google Sheet
  var slides = SlidesApp.getActivePresentation()
  const slide1 = slides.getSlides()[0]
  data.forEach(row => {
    slide = slide1.duplicate();
    slide.replaceAllText("{{cName}}", row[0])
    slide.replaceAllText("{{pName}}", row[1])
    slide.replaceAllText("{{wName}}", row[2])
    slide.replaceAllText("{{aName}}", row[3])
    slide.replaceAllText("{{sPlace}}", row[4])
  })
}