from webapp.model import db, Position


def save_positions(portfolio_id, instrument_id, amount, expected_yield,
                    average_price, current_price, lots):
    position_securities = Position(portfolio_id=portfolio_id, instrument_id=instrument_id,
                                    amount=amount, expected_yield=expected_yield,
                                    average_price=average_price, current_price=current_price,
                                    lots=lots)
    db.session.add(position_securities)
    db.session.commit()
