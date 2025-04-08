<%
out.println("<!DOCTYPE html>");
out.println("<html lang=\"en\">");
out.println("<html>");

// Head section
out.println("<head>");
out.println("      <!-- basic -->");
out.println("      <meta charset=\"utf-8\">");
out.println("      <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">");
out.println("      <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">");
out.println("      <!-- mobile metas -->");
out.println("      <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">");
out.println("      <meta name=\"viewport\" content=\"initial-scale=1, maximum-scale=1\">");
out.println("      <!-- site metas -->");
out.println("      <title>AQI</title>");
out.println("      <meta name=\"keywords\" content=\"\">");
out.println("      <meta name=\"description\" content=\"\">");
out.println("      <meta name=\"author\" content=\"\">");
out.println("      <!-- bootstrap css -->");
out.println("      <link rel=\"stylesheet\" type=\"text/css\" href=\"css/bootstrap.min.css\">");
out.println("      <!-- style css -->");
out.println("      <link rel=\"stylesheet\" type=\"text/css\" href=\"css/style.css\">");
out.println("      <!-- Responsive-->");
out.println("      <link rel=\"stylesheet\" href=\"css/responsive.css\">");
out.println("      <!-- fevicon -->");
out.println("      <link rel=\"icon\" href=\"images/fevicon.png\" type=\"image/gif\" />");
out.println("      <!-- font css -->");
out.println("      <link href=\"https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap\" rel=\"stylesheet\">");
out.println("      <!-- Scrollbar Custom CSS -->");
out.println("      <link rel=\"stylesheet\" href=\"css/jquery.mCustomScrollbar.min.css\">");
out.println("      <!-- Tweaks for older IEs-->");
out.println("      <link rel=\"stylesheet\" href=\"https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css\">");
out.println("<script src=\"https://code.jquery.com/jquery-3.2.1.slim.min.js\" integrity=\"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN\" crossorigin=\"anonymous\"></script>");
out.println("<script src=\"https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js\" integrity=\"sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q\" crossorigin=\"anonymous\"></script>");
out.println("<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js\" integrity=\"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl\" crossorigin=\"anonymous\"></script>");// Additional Style
out.println("   <style>");
out.println("      /* Set the container to take up the full height of the viewport */");
out.println("      #jspContent {");
out.println("          height: 100vh;");
out.println("          width: 100%; /* Adjust the width as needed */");
out.println("          margin: 0 auto; /* Center the content */");
out.println("          position: relative;");
out.println("          z-index: 1;");
out.println("      }");
out.println("   </style>");

// jQuery script
out.println("   <script src=\"https://code.jquery.com/jquery-3.6.4.min.js\"></script>");

out.println("    <meta charset=\"UTF-8\">");
out.println("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">");
out.println("    <title>Dashboard</title>");
out.println("    <style>");
out.println("        /* Add your styles for the grid here */");
out.println("        body {");
out.println("            margin: 0;");  // Remove default margin
out.println("        }");
out.println("        .chart-container {");
out.println("            display: grid;");
out.println("            grid-template-columns: repeat(2, 1fr);");  // Change to 2 columns
out.println("            grid-template-rows: repeat(4, 1fr);");      // Add 4 rows
out.println("            gap: 20px;");
out.println("            margin: 20px;");
out.println("            height: 100vh;");  // Set height to 100% of the viewport height
out.println("        }");
out.println("        .chart {");
out.println("            border: 0px solid #ddd;");
out.println("            padding: -50px;");
out.println("            width: 100%;");  // Set width to 100%
out.println("            height: 100%;");  // Set height to 100%
out.println("            box-sizing: border-box;");  // Include padding and border in total width and height
out.println("        }");
out.println("    </style>");


// Closing head section
out.println("</head>");

// Body section
out.println("<body>");
out.println("      <div class=\"header_section\">");
out.println("         <div class=\"container-fluid\">");
out.println("            <nav class=\"navbar navbar-expand-lg navbar-light bg-light\">");
out.println("               <a class=\"navbar-brand\" href=\"main.jsp\"><img src=\"images\\logo.png\"></a>");
out.println("               <button class=\"navbar-toggler\" type=\"button\" data-toggle=\"collapse\" data-target=\"#navbarSupportedContent\" aria-controls=\"navbarSupportedContent\" aria-expanded=\"false\" aria-label=\"Toggle navigation\">");
out.println("               <span class=\"navbar-toggler-icon\"></span>");
out.println("               </button>");
out.println("               <div class=\"collapse navbar-collapse\" id=\"navbarSupportedContent\">");
out.println("                  <ul class=\"navbar-nav ml-auto\">");
out.println("                     <li class=\"nav-item active\">");
out.println("                        <a class=\"nav-link\" href=\"main.jsp\">Home</a>");
out.println("                     </li>");
out.println("                     <li class=\"nav-item\">");
out.println("                        <a class=\"nav-link\" href=\"Map.jsp\">Map</a>");
out.println("                     </li>");
out.println("<li class=\"nav-item dropdown\">");
out.println("    <a class=\"nav-link dropdown-toggle\" href=\"#\" id=\"navbarDropdown\" role=\"button\" data-toggle=\"dropdown\" aria-haspopup=\"true\" aria-expanded=\"false\">");
out.println("        States");
out.println("    </a>");
out.println("    <div class=\"dropdown-menu\" aria-labelledby=\"navbarDropdown\" style=\"max-height: 350px; overflow-y: auto;\">");
out.println("        <a class=\"dropdown-item\" href=\"Ahmedabad.jsp\">Ahmedabad</a>");
out.println("        <a class=\"dropdown-item\" href=\"Aizawl.jsp\">Aizawl</a>");
out.println("        <a class=\"dropdown-item\" href=\"Amaravati.jsp\">Amaravati</a>");
out.println("        <a class=\"dropdown-item\" href=\"Amritsar.jsp\">Amritsar</a>");
out.println("        <a class=\"dropdown-item\" href=\"Bengaluru.jsp\">Bengaluru</a>");
out.println("        <a class=\"dropdown-item\" href=\"Bhopal.jsp\">Bhopal</a>");
out.println("        <a class=\"dropdown-item\" href=\"Brajrajnagar.jsp\">Brajrajnagar</a>");
out.println("        <a class=\"dropdown-item\" href=\"Chandigarh.jsp\">Chandigarh</a>");
out.println("        <a class=\"dropdown-item\" href=\"Chennai.jsp\">Chennai</a>");
out.println("        <a class=\"dropdown-item\" href=\"Coimbatore.jsp\">Coimbatore</a>");
out.println("        <a class=\"dropdown-item\" href=\"Delhi.jsp\">Delhi</a>");
out.println("        <a class=\"dropdown-item\" href=\"Ernakulam.jsp\">Ernakulam</a>");
out.println("        <a class=\"dropdown-item\" href=\"Gurugram.jsp\">Gurugram</a>");
out.println("        <a class=\"dropdown-item\" href=\"Guwahati.jsp\">Guwahati</a>");
out.println("        <a class=\"dropdown-item\" href=\"Hyderabad.jsp\">Hyderabad</a>");
out.println("        <a class=\"dropdown-item\" href=\"Jaipur.jsp\">Jaipur</a>");
out.println("        <a class=\"dropdown-item\" href=\"Jorapokhar.jsp\">Jorapokhar</a>");
out.println("        <a class=\"dropdown-item\" href=\"Kochi.jsp\">Kochi</a>");
out.println("        <a class=\"dropdown-item\" href=\"Kolkata.jsp\">Kolkata</a>");
out.println("        <a class=\"dropdown-item\" href=\"Lucknow.jsp\">Lucknow</a>");
out.println("        <a class=\"dropdown-item\" href=\"Mumbai.jsp\">Mumbai</a>");
out.println("        <a class=\"dropdown-item\" href=\"Patna.jsp\">Patna</a>");
out.println("        <a class=\"dropdown-item\" href=\"Shillong.jsp\">Shillong</a>");
out.println("        <a class=\"dropdown-item\" href=\"Talcher.jsp\">Talcher</a>");
out.println("        <a class=\"dropdown-item\" href=\"Thiruvananthapuram.jsp\">Thiruvananthapuram</a>");
out.println("        <a class=\"dropdown-item\" href=\"Visakhapatnam.jsp\">Visakhapatnam</a>");
out.println("        <!-- Add more states as needed -->");
out.println("    </div>");
out.println("</li>");
out.println("               </ul>");
out.println("               <form class=\"form-inline my-2 my-lg-0\">");
out.println("                  <div class=\"login_bt\">");
out.println("                     <ul>");
out.println("                        <li><a href=\"#\"><i class=\"fa fa-search\" aria-hidden=\"true\"></i></a></li>");
out.println("                     </ul>");
out.println("                  </div>");
out.println("               </form>");
out.println("            </div>");
out.println("         </nav>");
out.println("      </div>");
out.println("<div class=\"chart-container\">");
out.println("    <div class=\"chart\" id=\"no2_chart\">");
out.println("        <iframe src=\"Chandigarh_1.jsp\" width=\"100%\" height=\"500px\"></iframe>");
out.println("    </div>");
out.println("");
out.println("    <div class=\"chart\" id=\"o3_chart\">");
out.println("        <iframe src=\"Chandigarh_2.jsp\" width=\"100%\" height=\"500px\"></iframe>");
out.println("    </div>");
out.println("");
out.println("    <div class=\"chart\" id=\"so2_chart\">");
out.println("        <iframe src=\"Chandigarh_3.jsp\" width=\"100%\" height=\"500px\"></iframe>");
out.println("    </div>");
out.println("");
out.println("    <div class=\"chart\" id=\"pm2_5_chart\">");
out.println("        <iframe src=\"Chandigarh_4.jsp\" width=\"100%\" height=\"500px\"></iframe>");
out.println("    </div>");
out.println("");
out.println("    <div class=\"chart\" id=\"pm10_chart\">");
out.println("        <iframe src=\"Chandigarh_5.jsp\" width=\"100%\" height=\"500px\"></iframe>");
out.println("    </div>");
out.println("");
out.println("    <div class=\"chart\" id=\"nh3_chart\">");
out.println("        <iframe src=\"Chandigarh_6.jsp\" width=\"100%\" height=\"500px\"></iframe>");
out.println("    </div>");
out.println("");
out.println("    <div class=\"chart\" id=\"Parti_matt_chart\">");
out.println("        <iframe src=\"Chandigarh_7.jsp\" width=\"100%\" height=\"500px\"></iframe>");
out.println("    </div>");
out.println("");
out.println("    <div class=\"chart\" id=\"no_chart\">");
out.println("        <iframe src=\"Chandigarh_8.jsp\" width=\"100%\" height=\"500px\"></iframe>");
out.println("    </div>");
out.println("</div>");
out.println("");
out.println("   </div>");

out.println("</body>");
out.println("</html>");
%>