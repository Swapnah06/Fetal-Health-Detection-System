def get_abnormality_info(abnormality_type):
    remedies = {
        'anold chiari malformation': {
            'cause': 'Associated with genetic mutations, neural tube defects, or maternal exposure to harmful substances during pregnancy.',
            'prevention': 'Prenatal care, adequate folic acid intake, and avoiding teratogens during pregnancy.'
        },
        'arachnoid cyst': {
            'cause': 'May develop due to congenital malformations or trauma during fetal development.',
            'prevention': 'No specific prevention, but regular prenatal check-ups can help in early detection.'
        },
        'cerebellar hypoplasia': {
            'cause': 'Linked to genetic disorders, infections during pregnancy, or environmental toxins.',
            'prevention': 'Screening for infections, avoiding harmful substances, and ensuring proper prenatal nutrition.'
        },
        'cisterna magna': {
            'cause': 'Enlargement may result from genetic anomalies or structural brain malformations.',
            'prevention': 'Early genetic testing and regular prenatal ultrasounds.'
        },
        'colpocephaly': {
            'cause': 'Often caused by disruptions in brain development, including genetic factors or prenatal infections.',
            'prevention': 'Proper prenatal care and avoiding exposure to teratogens.'
        },
        'encephalocele': {
            'cause': 'Caused by neural tube defects or genetic factors.',
            'prevention': 'Folic acid supplementation and early prenatal screening.'
        },
        'holoprosencephaly': {
            'cause': 'Results from genetic mutations or maternal factors such as diabetes or infections.',
            'prevention': 'Managing maternal health conditions and regular prenatal screenings.'
        },
        'hydranencephaly': {
            'cause': 'Likely caused by vascular disruptions or infections during pregnancy.',
            'prevention': 'Infection prevention and regular monitoring of fetal development.'
        },
        'intracranial hemorrhage': {
            'cause': 'May occur due to trauma, infections, or coagulopathy in the fetus.',
            'prevention': 'Preventing maternal trauma and monitoring high-risk pregnancies.'
        },
        'intracranial tumor': {
            'cause': 'Rare, often linked to genetic mutations or fetal exposure to carcinogens.',
            'prevention': 'Avoiding teratogens and regular prenatal monitoring.'
        },
        'mild ventriculomegaly': {
            'cause': 'Caused by excessive cerebrospinal fluid due to genetic or environmental factors.',
            'prevention': 'Monitoring for infections and maintaining maternal health during pregnancy.'
        },
        'moderate ventriculomegaly': {
            'cause': 'Similar to mild ventriculomegaly but with more pronounced fluid buildup.',
            'prevention': 'Regular ultrasounds and management of maternal infections or conditions.'
        },
        'severe ventriculomegaly': {
            'cause': 'Significant fluid buildup caused by obstruction or abnormal brain development.',
            'prevention': 'Early intervention and close monitoring of high-risk pregnancies.'
        },
        'polencephaly': {
            'cause': 'Typically results from vascular events or infections affecting the brain during pregnancy.',
            'prevention': 'Infection control and good maternal health practices.'
        }
    }
    # Normalize input
    normalized_type = abnormality_type.strip().lower()
    return remedies.get(normalized_type, {'cause': 'Unknown', 'prevention': 'Unknown'})

# Example usage
abnormality_detected = 'Arachnoid Cyst'  # Example input (case-insensitive)
info = get_abnormality_info(abnormality_detected)
print("Cause:", info['cause'])
print("Prevention:", info['prevention'])
