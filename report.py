def generate_report(strength, issues):
    # Start with report header
    report_lines = ["\n---Security REPORT---"]
    
    # Add issues list if any problems found, otherwise show success message
    if issues:
        report_lines.append("---problems---\n")
        # Add each issue as a bullet point
        report_lines.extend([f'- {issue}' for issue in issues])
    else:
        report_lines.append("no problems found")
    
    # Join all lines with newlines and return as a single string
    return "\n".join(report_lines)