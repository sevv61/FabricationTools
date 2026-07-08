part = FabricationPartInfo(selection[0])

config = HangerConfiguration()

engine = HangerSpacingEngine(config)

validator = HangerValidator()

preview = HangerPreview()

points = engine.calculate(part.geometry)

points = validator.validate(
    points,
    part.geometry
)

forms.alert(
    preview.build_report(points)
)